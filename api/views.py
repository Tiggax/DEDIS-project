from django.urls import reverse_lazy
from django.shortcuts import render, HttpResponse, get_object_or_404
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm
from api.forms import ClimbUserCreationForm, ClimbUserUpdateForm
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Q, Func
from django.utils.html import strip_tags

import json
import re
from pages.models import *
from pages.forms import CommentForm



# Create your views here.

def index(req):
    ctx = {}
    ctx["title"] = "Alpine API Index"
    ctx["content"] = "api index"
    return render(req, "pages/example.html", ctx)

class SignUpView(CreateView):
    form_class = ClimbUserCreationForm
    success_url = reverse_lazy("accounts:login")
    template_name = "registration/signup.html"

@login_required
def user_settings(req):
    ctx = {}
    ctx["form"] = ClimbUserUpdateForm(instance = req.user)
    return render(req, "registration/profile.html", ctx)

@login_required
def update_user(req, field, target_user_id):
    ctx = {}
    ctx["messages"] = []
    ctx["target"] = field
    user = req.user
    
    try:
        target_user = ClimbUser.objects.get(id = target_user_id)
    except:
        return HttpResponse("<div>Target not found</div>")
    
    ctx["t_user"] = target_user
    ctx["value"] = getattr(target_user, field)
    
    match field:
        case "first_name" | "last_name" :
            field_widget = "widgets/forms/text.html"
        case "permission":
            ctx["disabled"] = True
            ctx["options"] = ClimbUser.PERMISSIONS 
            field_widget = "widgets/forms/options.html"
        case "rank":
            ctx["disabled"] = True
            ctx["options"] = ClimbUser.RANKS 
            field_widget = "widgets/forms/options.html"
        case _:
            field_widget = None
            return HttpResponse("<div>Cannot find widget</div>")

    match user.permission:
        case "U":
            if user.id != target_user.id:
                return HttpResponse(f"<div>You don't have access to this content</div>")
        case "A":
            if user.id != target_user.id:
                ctx["disabled"] = True
                return render(req, field_widget, ctx)
            pass
        case "M":
            if user.id != target_user.id or field == "rank":
                ctx["disabled"] = False
            pass

    # admin protection
    if target_user.is_staff or target_user.is_superuser:
        ctx["disabled"] = True

    # admin is god
    if user.is_staff or user.is_superuser:
        ctx["disabled"] = False

    if req.method == "GET":
        return render(req, field_widget, ctx)

    data = req.POST
    ctx["value"] = data[field] if field in data else "NODATA"


    # validate
    
    match field:
        case "first_name":
            user.first_name = data[field]
        case "last_name":
            user.last_name = data[field]
        case "rank":
            user.rank = data[field]
        case "permission":
            user.permission = data[field]
        case _:
            pass
    
    user.save()
    
    return render(req, field_widget, ctx)

class UpdatePassword(PasswordChangeView):
    form_class = PasswordChangeForm
    success_url = reverse_lazy("accounts:update")
    template_name = "registration/signup.html"


@login_required
def list_accounts(req):
    ctx = {}
    users = ClimbUser.objects.all()
    ctx["users"] = users
    return render(req, "registration/accounts.html", ctx)

def render_template(req, object, id, template):
    ctx = {}
    match object:
        case "NewsPost":
            ctx["data"] = get_object_or_404(NewsPost, pk = id)
        case "Comment":
            ctx["data"] = get_object_or_404(Comment, pk = id)
        case "Report":
            ctx["data"] = get_object_or_404(Report, pk = id)
        case _:
            pass
    print("request: {template} with {}", ctx["data"])
    return render(req, template, ctx)

# Comments

def comments(req, id):
    ctx = {}
    report = get_object_or_404(Report, id = id)
    ctx["data"] = report.comments.all().order_by("created")
    ctx["report"] = report

    return render(req, "widgets/comment/tree.html", ctx)


@login_required
def post_comment(req, id):
    ctx = {}
    report = get_object_or_404(Report, id = id)
    if req.method == "POST":
        form = CommentForm(req.POST)
        # validate
        if form.is_valid():
            data = form.cleaned_data
            c = Comment()
            c.content = data["content"]
            c.creator = req.user
            c.report_id = report
            c.save()
    else:
        form = CommentForm()
    
    ctx["form"] = form
    ctx["id"] = id

    return render(req, "widgets/comment/new_comment.html", ctx)

# News

def news(req):
    ctx = {}
    search_term = req.POST["search"] if req.POST["search"] else ""

    w_a_q_regex = r'"([^"]+)"|(\b\w+\b)'
    tags_regex = r'#(\w+)'
    key_val_regex = r'(\w+):(?:"([^"]+)"|(\w+))'

    w_a_q = re.findall(w_a_q_regex, search_term)
    tags = re.findall(tags_regex, search_term)
    key_vals = re.findall(key_val_regex, search_term)
    
    words = [match[1] for match in w_a_q if match[1]]
    quotes = [match[0] for match in w_a_q if match[0]]
    key_values = [(key, value or word) for key, value, word in key_vals]



    all_news = NewsPost.objects.all()
    
    query = Q()
    for word in words:
        query &= (Q(title__icontains = word ) | Q( content__icontains = word ))
    news = all_news.filter(query).distinct()

    if quotes:
        query = Q()
        for newspost in news:
            for quote in quotes:
                if (quote in strip_tags(newspost.content)) or (quote in newspost.title):
                    query |= Q(id = newspost.id)
        if query == Q():
            news = news.none()
        else:
            news = news.filter(query).distinct()

    if tags:
        matching_tags = Tag.objects.filter(tag__in = tags)
        news |= news.filter(tags__in = matching_tags).distinct()


    for key, val in key_values:
        match key:
            case "author":
                query = Q()
                for field in ["username", "first_name", "last_name"]:
                    query |= Q(**{f"{field}__icontains": val})
                users = ClimbUser.objects.filter(query)
                news |= all_news.filter( author__in = users ).distinct()
            case _:
                pass

    news = news.distinct().order_by("created").reverse()
    page_length = req.GET.get("page_count")
    paginator = Paginator(news, page_length if page_length else 10)
    page_number = req.GET.get("page")
    ctx["data"] =  paginator.get_page(page_number)
    ctx["search"] = json.dumps(search_term)
    return render(req, "widgets/news/tree.html", ctx)

def reports(req):
    ctx = {}
    search_term = req.POST["search"] if req.POST["search"] else ""

    w_a_q_regex = r'"([^"]+)"|(\b\w+\b)'
    tags_regex = r'#(\w+)'
    key_val_regex = r'(\w+):(?:"([^"]+)"|(\w+))'

    w_a_q = re.findall(w_a_q_regex, search_term)
    tags = re.findall(tags_regex, search_term)
    key_vals = re.findall(key_val_regex, search_term)
    
    words = [match[1] for match in w_a_q if match[1]]
    quotes = [match[0] for match in w_a_q if match[0]]
    key_values = [(key, value or word) for key, value, word in key_vals]



    all_reports = Report.objects.all()
    
    query = Q()
    for word in words:
        query &= (Q(title__icontains = word ) | Q( content__icontains = word ))
    reports = all_reports.filter(query).distinct()

    if quotes:
        query = Q()
        for report in reports:
            for quote in quotes:
                if (quote in strip_tags(report.content)) or (quote in report.title):
                    query |= Q(id = report.id)
        if query == Q():
            report = reports.none()
        else:
            report = reports.filter(query).distinct()

    if tags:
        matching_tags = Tag.objects.filter(tag__in = tags)
        reports |= reports.filter(tags__in = matching_tags).distinct()


    for key, val in key_values:
        match key:
            case "author":
                query = Q()
                for field in ["username", "first_name", "last_name"]:
                    query |= Q(**{f"{field}__icontains": val})
                users = ClimbUser.objects.filter(query)
                reports |= all_reports.filter( author__in = users ).distinct()
            case _:
                pass

    reports = reports.distinct().order_by("created").reverse()
    page_length = req.GET.get("page_count")
    paginator = Paginator(reports, page_length if page_length else 10)
    page_number = req.GET.get("page")
    ctx["data"] =  paginator.get_page(page_number)
    ctx["search"] = json.dumps(search_term)
    return render(req, "widgets/report/tree.html", ctx)
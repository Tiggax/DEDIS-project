from django.urls import reverse_lazy
from django.shortcuts import render, HttpResponse, get_object_or_404
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm
from api.forms import ClimbUserCreationForm, ClimbUserUpdateForm
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Q

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


class UpdateView(CreateView):
    form_class = ClimbUserUpdateForm
    success_url = reverse_lazy("accounts:update")
    template_name = "registration/signup.html"

class UpdatePassword(PasswordChangeView):
    form_class = PasswordChangeForm
    success_url = reverse_lazy("accounts:update")
    template_name = "registration/signup.html"


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
    

    terms = [match[0] or match[1] for match in w_a_q]
    key_values = [(key, value or word) for key, value, word in key_vals]

    print(key_values)


    all_news = NewsPost.objects.all()
    
    query = Q()
    for term in terms:
        query |= Q(title__icontains = term) | Q(content__icontains = term)

    news = all_news.filter(query).distinct()
    
    if tags:
        matching_tags = PostTag.objects.filter(tag__in = tags)
        news = all_news.filter(tags__in = matching_tags).distinct()



    for key, val in key_values:
        match key:
            case "author":
                users = ClimbUser.objects.filter(username__icontains = val)
                news |= all_news.filter( author__in = users ).distinct()
            case _:
                pass


    page_length = req.GET.get("page_count")
    paginator = Paginator(news, page_length if page_length else 10)
    page_number = req.GET.get("page")
    ctx["data"] =  paginator.get_page(page_number)
    ctx["search"] = search_term
    return render(req, "widgets/news/tree.html", ctx)
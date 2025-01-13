from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .models import NewsPost, Report, Comment
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from django.core.paginator import Paginator


# Create your views here.

def index(req):
    ctx = {}
    ctx["content"] = "pages index"
    news = NewsPost.objects.order_by("created")
    ctx["news_post"] = news.first()
    news = Report.objects.order_by("created")
    ctx["report"] = news.first()
    return render(req, "pages/home.html", ctx)

def about_us(req):
    ctx = {}
    ctx["content"] = "cntnt"
    return render(req, "pages/about_us.html", ctx)



@login_required
def logged_in_user_page(req):
    ctx = {}
    ctx["content"] = "user logged in"
    return render(req, "pages/example.html", ctx)

# Reports

def reports(req):
    ctx = {}
    reports = Report.objects.order_by("created")
    page_length = req.GET.get("page_count")
    paginator = Paginator(reports, page_length if page_length else 25)
    page_number = req.GET.get("page")
    ctx["reports"] = paginator.get_page(page_number)
    return render(req, "pages/reports.html", ctx)

def report(req, id):
    ctx = {}
    report = get_object_or_404(Report, id=id)
    ctx["report"] = report
    ctx["comments"] = report.comments.all()
    ctx["gallery"] = report.galleryimage_set.all()
    return render(req, "pages/report.html", ctx)

# News

def news(req):
    ctx = {}
    news = NewsPost.objects.order_by("created").reverse()
    ctx["default"] = news.first()
    return render(req, "pages/news.html", ctx)

def news_page(req, id):
    ctx = {}
    ctx["default"] = get_object_or_404(NewsPost, id = id)
    return render(req, "pages/news.html", ctx)
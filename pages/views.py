from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .models import NewsPost, Report
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login


# Create your views here.

def index(req):
    ctx = {}
    ctx["content"] = "pages index"
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
    return render(req, "pages/reports.html", ctx)

def report(req, id):
    ctx = {}
    ctx["data"] = get_object_or_404(Report, id=id)
    return render(req, "pages/report.html", ctx)

# News

def news(req):
    ctx = {}
    ctx["content"] = "add_news_here"
    ctx["posts"] =  NewsPost.objects.order_by("created")
    return render(req, "pages/news.html", ctx)

def get_news(req, id):
    ctx = {}
    ctx["data"] = get_object_or_404(NewsPost, id=id)
    return render(req, "pages/get_news.html", ctx)
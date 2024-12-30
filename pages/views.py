from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .models import NewsPost

# Create your views here.

def index(req):
    ctx = {}
    ctx["content"] = "pages index"
    return render(req, "pages/home.html", ctx)

def about_us(req):
    ctx = {}
    ctx["content"] = "cntnt"
    return render(req, "pages/about_us.html", ctx)

def news(req):
    ctx = {}
    ctx["content"] = "add_news_here"
    ctx["posts"] =  NewsPost.objects.order_by("created")
    return render(req, "pages/news.html", ctx)

def reports(req):
    ctx = {}
    ctx["content"] = "add_reports_here"
    return render(req, "pages/reports.html", ctx)

@login_required
def logged_in_user_page(req):
    ctx = {}
    ctx["content"] = "user logged in"
    return render(req, "pages/example.html", ctx)


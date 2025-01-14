from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .models import NewsPost, Report, Comment
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from django.core.paginator import Paginator

from pages.forms import ReportForm

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

# Reports

def reports(req):
    ctx = {}
    reports = Report.objects.order_by("created").reverse()
    ctx["default"] = reports.first()
    return render(req, "pages/reports.html", ctx)

def report(req, id):
    ctx = {}
    report = get_object_or_404(Report, id=id)
    ctx["default"] = report
    return render(req, "pages/reports.html", ctx)

@login_required
def report_form(req):
    ctx = {}
    ctx["form"] = ReportForm()
    if req.method == "GET":
        return render(req, "pages/new_report.html", ctx)
    form = ReportForm(req.POST)
    if form.is_valid():
        report = form.save(commit=False)
        report.author = req.user
        report.save()
        return redirect("pages:reports:get", id = report.id )
    
    ctx["form"] = form
    return render(req, "pages/new_report.html", ctx)

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
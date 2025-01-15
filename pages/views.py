from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .models import NewsPost, Report
from django.shortcuts import render, redirect, get_object_or_404

from pages.forms import ReportForm, NewsPostForm

# Create your views here.

def index(req):
    ctx = {}
    ctx["content"] = "pages index"
    news = NewsPost.objects.order_by("created").reverse()
    ctx["news_post"] = news.first()
    news = Report.objects.order_by("created").reverse()
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
    if not req.user.permission in ["A", "M"]:
        ctx["content"] = """
        <p>Nimate pravic za ustvarjanje Poročil. Če menite da je to napaka kontaktirajte osebje.</p>
        """
        return render(req, "pages/blank.html", ctx)
    
    ctx["form"] = ReportForm()
    if req.method == "GET":
        return render(req, "pages/reportForm.html", ctx)
    form = ReportForm(req.POST)
    if form.is_valid():
        report = form.save(commit=False)
        report.author = req.user
        report.save()
        return redirect("pages:reports:get", id = report.id )
    
    ctx["form"] = form
    return render(req, "pages/reportForm.html", ctx)

@login_required
def edit_report(req, id):
    ctx = {}
    report = get_object_or_404(Report, id = id)
    if (not req.user.permission in ["M"]) and req.user != report.author:
        ctx["content"] = """
        <p>Nimate pravic za spreminjanje tega Poročila. Če menite da je to napaka kontaktirajte osebje.</p>
        """
        return render(req, "pages/blank.html", ctx)
    ctx["form"] = ReportForm(instance=report)
    ctx["default"] = report
    if req.method == "GET":
        return render(req, "pages/reportForm.html", ctx)
    
    form = ReportForm(req.POST, instance=report)

    if form.is_valid():
        report = form.save(commit=False)
        report.author = req.user
        report.save()
        return redirect("pages:reports:get", id = report.id )

    return render(req, "pages/reportForm.html", ctx)

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

@login_required
def newspost_form(req):
    ctx = {}
    if not req.user.permission in ["M"]:
        ctx["content"] = """
        <p>Nimate pravic za ustvarjanje novic. Če menite da je to napaka kontaktirajte osebje.</p>
        """
        return render(req, "pages/blank.html", ctx)
        
    ctx["form"] = NewsPostForm()
    if req.method == "GET":
        return render(req, "pages/newsPostForm.html", ctx)
    form = NewsPostForm(req.POST)
    if form.is_valid():
        news_post = form.save(commit=False)
        news_post.author = req.user
        news_post.save()
        return redirect("pages:news:get", id = news_post.id )
    
    ctx["form"] = form
    return render(req, "pages/newsPostForm.html", ctx)

@login_required
def edit_newspost(req, id):
    ctx = {}
    news_post = get_object_or_404(NewsPost, id = id)
    if (not req.user.permission in ["M"]) and req.user != news_page.author:
        ctx["content"] = """
        <p>Nimate pravic za spreminjanje te novice. Če menite da je to napaka kontaktirajte osebje.</p>
        """
        return render(req, "pages/blank.html", ctx)
    
    ctx["form"] = NewsPostForm(instance= news_post)
    if req.method == "GET":
        return render(req, "pages/newsPostForm.html", ctx)
    
    form = NewsPostForm(req.POST, instance=news_post)

    if form.is_valid():
        news_post = form.save(commit=False)
        news_post.author = req.user
        news_post.save()
        return redirect("pages:news:get", id = news_post.id )

    return render(req, "pages/newsPostForm.html", ctx)
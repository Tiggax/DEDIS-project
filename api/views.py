from django.shortcuts import render

# Create your views here.

def index(req):
    ctx = {}
    ctx["title"] = "Alpine API Index"
    ctx["content"] = "api index"
    return render(req, "pages/example.html", ctx)
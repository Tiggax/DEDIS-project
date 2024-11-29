from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(req):
    ctx = {}
    ctx["title"] = "pages Index"
    ctx["content"] = "pages index"
    return render(req, "pages/example.html", ctx)

@login_required
def logged_in_user_page(req):
    ctx = {}
    ctx["title"] = "user loged in "
    ctx["content"] = "user logged in"
    return render(req, "pages/example.html", ctx)
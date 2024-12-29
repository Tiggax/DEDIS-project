from django.urls import reverse_lazy
from django.shortcuts import render, HttpResponse
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm

import json



# Create your views here.

def index(req):
    ctx = {}
    ctx["title"] = "Alpine API Index"
    ctx["content"] = "api index"
    return render(req, "pages/example.html", ctx)

class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"


def render_template(req, template):
    ctx = {}
    
    if req.method == "POST":
        ctx["data"] = json.loads(req.body)
    else:
        ctx["data"] = json.dumps("Only POST allowed")
        print(f"NOT POST REQUEST")
        return HttpResponse(ctx["data"], 'application/json', charset='utf-8')
    print("request: {template} with {}", ctx["data"])
    return render(req, template, ctx)


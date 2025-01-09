from django.urls import reverse_lazy
from django.shortcuts import render, HttpResponse, get_object_or_404
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm
from api.forms import ClimbUserCreationForm, ClimbUserUpdateForm
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.forms import PasswordChangeForm


import json
from pages.models import *



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
    
    if req.method == "POST":
        try:

            ctx["data"] = json.loads(req.body)
        
        except Exception as e:
            pass
            # ctx["data"] = json.dumps(e)
        match object:
            case "NewsPost":
                ctx["data"] = get_object_or_404(NewsPost, pk = id)
            case "Comment":
                ctx["data"] = get_object_or_404(Comment, pk = id)
            case "Report":
                ctx["data"] = get_object_or_404(Report, pk = id)
            case _:
                pass
        
    else:
        ctx["data"] = json.dumps("Only POST allowed")
        print(f"NOT POST REQUEST")
        return HttpResponse(ctx["data"], 'application/json', charset='utf-8')
    print("request: {template} with {}", ctx["data"])
    return render(req, template, ctx)

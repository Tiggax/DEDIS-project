from django.urls import reverse_lazy
from django.shortcuts import render, HttpResponse, get_object_or_404
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm
from api.forms import ClimbUserCreationForm

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



def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
    else:
        form = CustomUserCreationForm()
    
    return render(request, 'registration/register.html', {'form': form})
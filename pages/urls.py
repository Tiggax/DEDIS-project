from django.urls import path, include
from . import views


urlpatterns = [
    path("", views.index, name="pages"),
    path('loged', views.logged_in_user_page),
]

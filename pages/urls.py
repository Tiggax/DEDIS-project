from django.urls import path, include
from . import views


urlpatterns = [
    path("", views.index, name="home"),
    path('loged', views.logged_in_user_page),
    path("about_us", views.about_us, name="about_us"),
    path("news", views.news, name="news"),
    path("reports", views.reports, name="reports")
]

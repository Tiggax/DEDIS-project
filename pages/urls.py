from django.urls import path, include
from . import views

app_name = "pages"
urlpatterns = [
    path("", views.index, name="home"),
    path("about_us", views.about_us, name="about_us"),
    path("news", views.news, name="news"),
    path("news/<uuid:id>", views.news_page, name = "news_page"),
    path("reports", views.reports, name="reports"),
    path("reports/<uuid:id>", views.report, name="report"),
]

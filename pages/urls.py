from django.urls import path, include
from . import views

app_name = "pages"

reports =([
    path("", views.reports, name="all"),
    path("<uuid:id>", views.report, name="get"),
    path("create", views.report_form, name="create")
], "reports")

urlpatterns = [
    path("", views.index, name="home"),
    path("about_us", views.about_us, name="about_us"),
    path("news", views.news, name="news"),
    path("news/<uuid:id>", views.news_page, name = "news_page"),
    path("reports/", include(reports)),
]

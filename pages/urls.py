from django.urls import path, include
from . import views

app_name = "pages"

reports = ([
    path("", views.reports, name="all"),
    path("<uuid:id>", views.report, name="get"),
    path("create", views.report_form, name="create"),
    path("edit/<uuid:id>", views.edit_report, name="edit"),
], "reports")

news = ([
    path("", views.news, name="all"),
    path("<uuid:id>", views.news_page, name = "get"),
    path("create", views.newspost_form, name = "create"),
    path("edit/<uuid:id>", views.edit_newspost, name="edit"),
], "news")

urlpatterns = [
    path("", views.index, name="home"),
    path("about_us", views.about_us, name="about_us"),
    path("news/", include(news)),
    path("reports/", include(reports)),
]

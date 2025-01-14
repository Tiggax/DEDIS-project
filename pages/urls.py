from django.urls import path, include
from . import views

app_name = "pages"

reports = ([
    path("", views.reports, name="all"),
    path("<uuid:id>", views.report, name="get"),
    path("create", views.report_form, name="create")
], "reports")

news = ([
    path("", views.news, name="all"),
    path("<uuid:id>", views.news_page, name = "get"),
], "news")

urlpatterns = [
    path("", views.index, name="home"),
    path("about_us", views.about_us, name="about_us"),
    path("news", include(news)),
    path("reports/", include(reports)),
]

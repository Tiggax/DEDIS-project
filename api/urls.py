"""
URL configuration for alpine project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static
import pages.urls


from . import views

accounts = ([
    path('signup/', views.SignUpView.as_view(), name = "signup"),
    path('update/', views.UpdateView.as_view(), name = "update"),
    path('password/', views.UpdatePassword.as_view(), name="password"),
    path("", include("django.contrib.auth.urls")),
], "accounts")

apis = ([
    path('', views.index),
    path('render/<str:object>/<int:id>/<path:template>', views.render_template, name="render"),
], "api")



urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(apis)),
    path('api/summernote/', include('django_summernote.urls')), # manual move out of "api:..."
    path('accounts/',include(accounts)),
    path('', include("pages.urls"))
]

if settings.DEBUG:
    urlpatterns += static(
        settings.STATIC_URL,
        document_root = settings.STATIC_ROOT
    )
urlpatterns += static(
        settings.MEDIA_URL,
        document_root = settings.MEDIA_ROOT
    )
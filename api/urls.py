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
    path('profile/', views.user_settings, name = "profile" ),
    path('update/<str:field>/<uuid:target_user_id>', views.update_user, name = "update"),
    path('password/', views.UpdatePassword.as_view(), name="password"),
    path("", include("django.contrib.auth.urls")),
    path("", views.list_accounts, name = ""),
], "accounts")

mountains = ([
    path('search/', views.mountains, name="search"),
    path('new', views.create_mountain, name="new"),
], "mountains")

routes = ([
    path('search/', views.routes, name="search"),
    path('new', views.create_route, name="new"),
],"routes")

apis = ([
    path('render/<str:object>/<uuid:id>/<path:template>', views.render_template, name="render"),
    path('comments/<uuid:id>', views.comments, name="comments"),
    path('comment/<uuid:id>', views.post_comment, name="post_comment"),
    path('news', views.news, name="news"),
    path('reports', views.reports, name="reports"),
    path('mountains/', include(mountains)),
    path('routes/', include(routes)),
], "api")



urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(apis)),
    path('api/summernote/', include('django_summernote.urls')), # manual move out of "api:..."
    path('accounts/',include(accounts)),
    path('', include("pages.urls")),
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
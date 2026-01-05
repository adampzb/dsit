"""reddit_clone URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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

import os

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path, re_path
from django.views.generic import TemplateView
from django.views.static import serve
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title="Django Reddit API",
        default_version="v1",
        description="API documentation for the reddit clone project",
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)


# Serve Angular app from dist directory
angular_index = TemplateView.as_view(template_name="angular/index.html")

urlpatterns = [
    path("admin/", admin.site.urls),
    # Serve Angular app for all non-API, non-admin routes
    path("", angular_index, name="angular_home"),
    path("django_reddit/", angular_index, name="angular_app"),
    path("django_reddit/<path:path>", angular_index, name="angular_routes"),
    # path('accounts/', include('allauth.urls')),
    re_path(r"^dj-rest-auth/", include("dj_rest_auth.urls")),
    re_path(r"^dj-rest-auth/registration/", include("dj_rest_auth.registration.urls")),
    path("api/v1/", include("posts.urls")),
    path("api/v1/", include("tags.urls")),
    path("api/v1/", include("groups.urls")),
    path("api/v1/", include("profiles.urls")),
    path("api/v1/", include("reports.urls")),
    path(
        "api/swagger/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="swagger-docs",
    ),
    path(
        "api/redoc/",
        schema_view.with_ui("redoc", cache_timeout=0),
        name="redoc-docs",
    ),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Serve Angular static files from django_reddit path
if settings.DEBUG:
    # First try to serve actual files
    urlpatterns += [
        re_path(r"^django_reddit/(?P<path>.+\.(js|css|png|jpg|jpeg|gif|svg|woff|woff2|ttf|eot))$", serve, {
            "document_root": os.path.join(settings.BASE_DIR, "static", "frontend", "reddit-app", "angular", "dist"),
        }),
    ]
    # Then serve index.html for all other routes (Angular routing)
    urlpatterns += [
        re_path(r"^django_reddit/(?:.*)?$", angular_index),
    ]

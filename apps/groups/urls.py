from django.urls import include, path

from .router import group_router, router

urlpatterns = [
    path("", include(router.urls)),
    path("", include(group_router.urls)),
]

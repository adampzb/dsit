from django.urls import include, path

from .router import post_router, router

urlpatterns = [
    path("", include(router.urls)),
    path("", include(post_router.urls)),
]

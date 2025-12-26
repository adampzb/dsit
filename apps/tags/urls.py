from django.urls import include, path
from tags.router import router

urlpatterns = [
    path("", include(router.urls)),
]

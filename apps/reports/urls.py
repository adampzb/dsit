from django.urls import include, path
from reports.router import router

urlpatterns = [
    path("", include(router.urls)),
]

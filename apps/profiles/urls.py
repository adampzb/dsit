from django.urls import include, path, re_path
from profiles.views import IsAuthenticatedView

from .router import router

urlpatterns = [
    path("", include(router.urls)),
    re_path(
        r"^is_authenticated/$",
        IsAuthenticatedView.as_view(),
        name="is_authenticated",
    ),
]

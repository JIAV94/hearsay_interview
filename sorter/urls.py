from django.urls import path
from .views import SortKeysView

urlpatterns = [
    path("sortkeys/", SortKeysView.as_view(), name="sort-keys"),
]

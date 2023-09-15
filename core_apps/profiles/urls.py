from rest_framework.routers import DefaultRouter
from django.urls import (
    path,
    include,
)

from core_apps.profiles import views

app_name = "profiles"

urlpatterns = [
    path("all/", views.ProfilesApiView.as_view(), name="all_profiles"),
    path("<str:username>/get", views.ProfileApiView.as_view(), name="single_profile"),
    path("<str:username>/update", views.UpdateProfileApiView.as_view(), name="update_profile"),
]

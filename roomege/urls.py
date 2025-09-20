from django.urls import path

from . import views

app_name = "roomege"
urlpatterns = [
        path("profile/<int:pk>", views.ProfileView.as_view(), name="profile"),
        path("create_profile/", views.CreateProfileView.as_view(), name="create_profile"),
]
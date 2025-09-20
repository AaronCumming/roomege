from django.urls import path

from . import views

app_name = "roomege"
urlpatterns = [
        path("profile/<int:pk>", views.ProfileView.as_view(), name="profile"),
        path("create_profile/", views.CreateUserView.as_view(), name="create_profile"),
        path("matches/", views.MatchesView.as_view(), name="matches"),
        
]
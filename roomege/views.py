"""
views.py
Aaron Cumming
2025-09-25
"""

from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse, reverse_lazy
from django.views import generic
from django.contrib.auth import logout

from .models import CustomUser, Social

# Create your views here.
class ProfileView(generic.DetailView):
    """Displays profile."""
    model = CustomUser
    template_name = "roomege/profile.html"


class CreateUserView(generic.CreateView):
    """User can create a parent chirp."""
    model = CustomUser
    fields = [
        'first_name', 'last_name', 'age', 'grade', 'city', 'state',
        'religion', 'church', 'bedtime', 'waketime', 'room_state', 'social_area',
        'dishes_scenario', 'late_hw', 'relationship_expectation', 'image'
    ]
    template_name = "roomege/create_profile.html"
    success_url = reverse_lazy("roomege:matches")

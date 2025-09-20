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
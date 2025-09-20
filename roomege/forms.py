from django import forms
from .models import CustomUser, Social

# For the sake of simplicity, fields are being input directily in views.py instead of using forms here.
# Given more time, I would refactor views.py to use these forms.

class CustomUserCreationForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = [
            'username', 'password', 'first_name', 'last_name', 'email'
        ]
        widgets = {
            'password': forms.PasswordInput(),
        }

class CustomUserPreferencesForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = [
            'age', 'grade', 'city', 'state', 'religion', 'church', 'bedtime',
            'waketime', 'room_state', 'social_area', 'dishes_scenario',
            'late_hw', 'relationship_expectation'
        ]
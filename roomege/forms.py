from django import forms
from .models import CustomUser, Social

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
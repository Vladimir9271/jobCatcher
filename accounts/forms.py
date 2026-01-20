from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class RegisterForm(UserCreationForm):
    role = forms.ChoiceField(
        choices=CustomUser.ROLE_CHOICES,
        widget=forms.RadioSelect,
        label="Кто вы?"
    )

    class Meta:
        model = CustomUser
        fields = ['username', 'password1', 'password2', 'role']
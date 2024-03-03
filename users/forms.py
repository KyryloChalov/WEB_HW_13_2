from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class LoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ["username", "password"]


class RegistrationForm(UserCreationForm):
    username = forms.CharField(max_length=100, required=True, widget=forms.TextInput())

    email = forms.CharField(max_length=100, required=True, widget=forms.TextInput())

    password1 = forms.CharField(
        max_length=50, required=True, widget=forms.PasswordInput()
    )

    password2 = forms.CharField(
        max_length=50, required=True, widget=forms.PasswordInput()
    )

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

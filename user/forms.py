from django import forms 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model 


class RegisterForm(UserCreationForm):
    email = forms.CharField(widget=forms.EmailInput(attrs={"class": "form-control", "placeholder": "Enter email-address"}))
    username = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter username"}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={"class": "form-control", "placeholder": "Enter password"}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={"class": "form-control", "placeholder": "Re-enter password"}))
    class Meta:
        model = get_user_model()
        fields = ["email", "username", "password1", "password2"]
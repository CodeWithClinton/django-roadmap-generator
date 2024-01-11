from django import forms 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model 
from .models import Profile


class RegisterForm(UserCreationForm):
    email = forms.CharField(widget=forms.EmailInput(attrs={"class": "form-control", "placeholder": "Enter email-address"}))
    username = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter username"}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={"class": "form-control", "placeholder": "Enter password"}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={"class": "form-control", "placeholder": "Re-enter password"}))
    class Meta:
        model = get_user_model()
        fields = ["email", "username", "password1", "password2"]
        
        
        
        
class UpdateProfileForm(forms.ModelForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control", "placeholder": "Enter firstname"}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control", "placeholder": "Enter lastname"}))
    username = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control", "placeholder": "Enter username"}))
    email = forms.CharField(widget=forms.EmailInput(attrs={"class":"form-control", "placeholder": "Enter email address"}))
    image = forms.ImageField(required=False, widget=forms.FileInput(attrs={"class": "form-control", "placeholder": "Upload image"}))
    profession = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control", "placeholder": "Enter profession"}))
    twitter = forms.CharField(required=False, widget=forms.URLInput(attrs={"class": "form-control", "placeholder": "Enter Twitter URL"}))
    github = forms.CharField(required=False, widget=forms.URLInput(attrs={"class": "form-control", "placeholder": "Enter GitHub URL"}))
    linkedin = forms.CharField(required=False, widget=forms.URLInput(attrs={"class": "form-control", "placeholder": "Enter LinkedIn URL"}))
    bio = forms.CharField(widget=forms.Textarea(attrs={"class":"form-control", "placeholder": "Enter bio"}))
    
    class Meta:
        model = Profile 
        exclude = ["user"]
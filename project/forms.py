from django import forms 
from .models import Project 


class ProjectForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control", "placeholder":"Enter title"}))
    description = forms.CharField(widget=forms.Textarea(attrs={"class": "form-control", "placeholder":"Enter body"}))
    image = forms.ImageField(widget=forms.FileInput(attrs={"class": "form-control", "placeholder":"Add image"}))
    link = forms.CharField(required=False, widget=forms.URLInput(attrs={"class": "form-control", "placeholder": "Enter project url"}))
    github_link = forms.CharField(required=False, widget=forms.URLInput(attrs={"class": "form-control", "placeholder": "Enter github url"}))
    class Meta:
        model = Project
        exclude = ["slug", "owner"]
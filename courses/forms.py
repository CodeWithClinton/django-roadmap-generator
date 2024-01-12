from django import forms 
from .models import CourseAlert 

class CourseAlertForm(forms.ModelForm):
    email = forms.CharField(widget=forms.EmailInput(attrs={"class":"form-control", "placeholder": "Email address..."}))
    class Meta:
        model = CourseAlert 
        fields = ["email"]

    
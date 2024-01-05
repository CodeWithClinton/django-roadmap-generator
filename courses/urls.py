from django.urls import path 
from .import views  

app_name = 'courses'

urlpatterns = [
    path("", views.index, name="index"), 
    path("courses/<slug:slug>", views.detail, name="course"),
    path("ask_openai", views.ask_openai)
]
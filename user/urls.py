from django.urls import path 
from .import views  

app_name = 'auth'

urlpatterns = [
    path("index", views.index, name="index"),  
    path("register", views.sign_up, name="register"),
    path("logout", views.sign_out, name="logout"),
    path("profile", views.profile, name="profile"),
    path("take-quiz/<int:pk>", views.quiz_profile, name="q-profile"),
    path("fetch_quiz", views.fetch_quiz, name="fetch-quiz")
]
from django.urls import path 
from .import views  

app_name = 'auth'

urlpatterns = [

    path("register", views.sign_up, name="register"),
    path("login", views.sign_in, name="signin"),
    path("logout", views.sign_out, name="logout"),
    path("profile", views.profile, name="profile"),
    path("update-profile", views.update_profile, name="update-profile"),
    path("take-quiz/<int:pk>", views.quiz_profile, name="q-profile"),
    path("fetch_quiz", views.fetch_quiz, name="fetch-quiz"),
    path("profiles", views.profile_list, name="profile-list"),
    path("profiles/<slug:username>", views.profile_detail, name='profile-detail')
]
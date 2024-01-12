from django.urls import path 
from . import views 

app_name = "project"

urlpatterns = [
    path("create", views.add_project, name="create"),
    path("update/<slug:slug>", views.update_project, name="update")
]


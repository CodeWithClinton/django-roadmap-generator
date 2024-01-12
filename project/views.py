from django.shortcuts import render, redirect
from .forms import ProjectForm
from django.utils.text import slugify
from django.contrib import messages
from .models import Project
# Create your views here.

def add_project(request):
    user = request.user
    form = ProjectForm()
    if request.method == "POST":
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.owner = user 
            project.slug = slugify(request.POST['title'])
            project.save()
            messages.success(request, "Your project has been added successfully")
            return redirect("auth:profile")
    context={"form": form}
    return render(request, "project/add-project.html", context)


def update_project(request, slug):
    project = Project.objects.get(slug=slug)
    upt = "update"
    form = ProjectForm(instance = project)
    if request.method == "POST":
        form = ProjectForm(request.POST, request.FILES,  instance=project)
        if form.is_valid():
            project = form.save(commit=False)
            project.slug = slugify(request.POST['title'])
            project.save()
            messages.success(request, "Your project has been updated successfully!!")
            return redirect("auth:profile")
    context = {"form": form, "upt":upt}
    return render(request, "project/add-project.html", context)


# def delete_project(request, slug):
#     context = {"form": form, "upt":upt}
#     return render(request, "project/add-project.html", context)
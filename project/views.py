from django.shortcuts import render, redirect
from .forms import ProjectForm
from django.utils.text import slugify
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Project
# Create your views here.

@login_required(login_url='auth:register')
def add_project(request):
    if request.user.passed:
        user = request.user
        form = ProjectForm()
        if request.method == "POST":
            form = ProjectForm(request.POST, request.FILES)
            if form.is_valid():
                project = form.save(commit=False)
                project.owner = user 
                project.slug = slugify(request.POST['title'])
                project.save()
                user.project = True 
                user.save()
                messages.success(request, "Your project has been added successfully")
                return redirect("auth:profile")
    else:
        messages.warning(request, "You are not yet eligible to add your projects")
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
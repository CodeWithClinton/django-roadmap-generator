from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from courses.models import UserCourse
# Create your views here.

def index(request):
    return render(request, "user/index.html")

def GoogleRedirectView(request):
    # Your logic to skip the login view and redirect to Google account selection
    return redirect('https://accounts.google.com/AccountChooser')

def sign_up(request):
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            
            email = request.POST['email']
            password = request.POST['password1']
            
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, "Account created successfully")
                return redirect("auth:index")
            
    context = {"form": form}
    return render(request, "user/signup.html", context)


def sign_out(request):
    logout(request)
    
@login_required(login_url='auth:register')
def profile(request):
    user = request.user
    user_courses = UserCourse.objects.filter(user=user)
    context = {"user": user, "u_courses": user_courses}
    return render(request, "user/profile.html", context)
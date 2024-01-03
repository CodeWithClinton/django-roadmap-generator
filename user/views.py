from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

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
from django.shortcuts import render, redirect
from .forms import RegisterForm, UpdateProfileForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from courses.models import UserCourse, Quiz, QuizOption, UserScore
from django.http import JsonResponse
from .models import Profile
from project.models import Project
from django.contrib.auth import get_user_model
import json
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
                return redirect("courses:index")
            
    context = {"form": form}
    return render(request, "user/signup.html", context)


def sign_in(request):
    if request.method == 'POST':
        email = request.POST["email"]
        password = request.POST["password"]
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            # messages.success(request, "Account created successfully")
            return redirect("courses:index")
    context = {}
    return render(request, "user/signin.html", context)
    


@login_required(login_url='auth:register')
def update_profile(request):
    user = request.user 
    profile = Profile.objects.get(user=user)
    form = UpdateProfileForm(instance=profile)
    if request.method == 'POST':
        form = UpdateProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, "Profile updated successfully!")
            return redirect("auth:profile")
    context = {"form": form, "profile": profile}
    return render(request, "user/update_profile.html", context)
    



def sign_out(request):
    logout(request)
    return redirect("courses:index")
    
@login_required(login_url='auth:register')
def profile(request):
    user = request.user
    profile = Profile.objects.get(user=user)
    projects = Project.objects.filter(owner=user)
    user_courses = UserCourse.objects.filter(user=user)
    context = {"user": user, "u_courses": user_courses, "profile": profile, "projects": projects}
    return render(request, "user/profile.html", context)


def profile_list(request):
    user = get_user_model()
    all_user = user.objects.filter(passed=True, project=True)
    # user_courses = UserScore.objects.filter(user=user.id, score__gte=80)
    context = {"all_users": all_user}
    return render(request, "user/profile_list.html", context)


def profile_detail(request, username):
    profile = Profile.objects.get(user__username=username)
    projects = Project.objects.filter(owner=profile.user)
    context = {"profile": profile, "projects": projects} 
    return render(request, "user/profile_detail.html", context)
    


@login_required(login_url='auth:register')
def quiz_profile(request, pk):
    user = request.user
    user_course = UserCourse.objects.get(id=pk)
    user_score=""
    try:
        user_score = UserScore.objects.get(user=user, user_course=user_course)
    except UserScore.DoesNotExist:
        user_score=""
    quiz = Quiz.objects.filter(user_course=user_course)
    
    if request.method == 'POST':
        data = json.loads(request.body)
        score = int(data["user_score"])
        if score >= 80:
            user.passed=True 
        else:
            user.passed=False 
        user.save()
        try:
            user_score = UserScore.objects.get(user=user, user_course=user_course)
            if user_score:
                user_score.score = score 
                user_score.save()
            
        except UserScore.DoesNotExist:
            user_score = UserScore.objects.create(user_course=user_course, user=user, score=score)
        
        return JsonResponse(score, safe=False)
 
    else:
    
        context = {"user": user, "q_course": user_course, "quiz":quiz, "user_score":user_score}
        return render(request, "user/quiz_profile.html", context)



def quiz_score(request, pk):
    user = request.user
    user_course = UserCourse.objects.get(id=pk)
    user_score = UserScore.objects.get(user=user, user_course=user_course)
    context = {"user": user, "user_course": user_course, "user_score":user_score}
    return render(request, "user/quiz_profile.html", context)


def fetch_quiz(request):
    data = json.loads(request.body)
    user_course_id = data['user_course_Id']
    user_course = UserCourse.objects.get(id=user_course_id)
    quizes = Quiz.objects.filter(user_course=user_course)
    new_quizzes = [
    {"id":quiz.id, "question": quiz.question, "options": [option.option for option in quiz.options.all()]}
    for quiz in quizes
    ]
    print(new_quizzes)
    return JsonResponse(new_quizzes, safe=False)
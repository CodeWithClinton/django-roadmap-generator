from django.shortcuts import render, redirect
from decouple import config, Csv
from openai import OpenAI
from django.http import JsonResponse
from .models import Course, Schedule, MiniSchedule, UserCourse, Roadmap, Quiz, QuizOption, Category
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from .forms import CourseAlertForm
from django.contrib import messages
import json

client = OpenAI(api_key=config("OPENAI_API_KEY"),)

# Create your views here.

def index(request):
    # Initialize form and fetch all courses
    form = CourseAlertForm()
    courses = Course.objects.all()
    paginator = Paginator(courses, 3)
    page = request.GET.get("page")
    
    # Handle form submission
    if request.method == 'POST':
        form = CourseAlertForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Awesome, you will be alerted for upcoming courses")
            return redirect("courses:index")
    
    # Paginate courses
    try:  
        courses = paginator.page(page)
    except PageNotAnInteger:
        courses = paginator.page(1)
    except EmptyPage:
        courses = paginator.page(paginator.num_pages)
    
    context = {"courses": courses, "paginator": paginator, "form": form}
    return render(request, "courses/index.html", context)


def detail(request, slug):
    course = Course.objects.get(slug=slug)
    cat_courses = Course.objects.filter(category__title=course.category.title).exclude(id=course.id)
    user_course = ""
    roadmap_num = 0
    
    if request.user.is_authenticated:
        try:
            user_course = UserCourse.objects.get(user=request.user, course=course)
            roadmap_num = Roadmap.objects.filter(user_course=user_course).count()
        except UserCourse.DoesNotExist:
            pass
    
    schedules = Schedule.objects.all()
    context = {"course": course, "schedules": schedules, "user_course": user_course, "r_num": roadmap_num, "c_courses": cat_courses}
    
    return render(request, "courses/detail.html", context)


@login_required(login_url='auth:register')
def ask_openai(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        course_id = data["c_id"]
        schedule_id = data["sch_id"]
        mini_schedule_id = data["mini_sch_id"]
        
        course = Course.objects.get(id=course_id)
        course_label = Course.objects.get(id=course_id).label
        schedule = Schedule.objects.get(id=schedule_id)
        mini_schedule = MiniSchedule.objects.get(id=mini_schedule_id)
        
        print(f"{course_label} roadmap for {mini_schedule} {schedule}")
        
        completion = client.chat.completions.create(
            model="gpt-3.5-turbo-1106",
            response_format={ "type": "json_object" },
            messages=[
                {"role": "system", "content": f"""
                 
                 You are a helpful assistant designed to output JSON, 
                 JSON output should contain title, 
                 duration, frequency, learning_roadmap, quiz. learning_roadmap should be an array of topics to learn,
                 quiz should be an array of object consisiting of 7 questions, options and answer.
                 """
                 },
                {"role": "user", "content": f"comprehensive {course_label} roadmap for {mini_schedule} {schedule} every {schedule}"}
            ]
        )
        
        new_output = completion.choices[0].message.content
        db_output = json.loads(new_output)
        
        if db_output:
            try:
                user_course = UserCourse.objects.get(user=request.user, course=course)
                user_course.schedule=schedule 
                user_course.mini_schedule=mini_schedule 
                user_course.save()
                roadmap = Roadmap.objects.filter(user_course=user_course)
                quiz = Quiz.objects.filter(user_course=user_course)
                
                if roadmap.exists():
                    roadmap.delete()
                    
                if quiz.exists():
                    quiz.delete()

                new_roadmap = [Roadmap(title=r, user_course=user_course) for r in db_output["learning_roadmap"]]
                Roadmap.objects.bulk_create(new_roadmap)
                
                # Creating the quiz questions
                user_quizzes = db_output["quiz"]
                
                for u in user_quizzes:
                    user_quiz = Quiz.objects.create(question=u["question"], user_course=user_course, answer=u["answer"])
                    for option in u["options"]:
                        QuizOption.objects.create(option=option, quiz=user_quiz)
                        
            except UserCourse.DoesNotExist:
                user_course = UserCourse.objects.create(user=request.user, course=course, schedule=schedule, mini_schedule=mini_schedule)

                roadmap = [Roadmap(title=r, user_course=user_course) for r in db_output["learning_roadmap"]]
                Roadmap.objects.bulk_create(roadmap)
                
                # Creating the quiz questions
                user_quizzes = db_output["quiz"]
                
                for u in user_quizzes:
                    user_quiz = Quiz.objects.create(question=u["question"], user_course=user_course, answer=u["answer"])
                    for option in u["options"]:
                        QuizOption.objects.create(option=option, quiz=user_quiz)
        
        return JsonResponse(new_output, safe=False)

    
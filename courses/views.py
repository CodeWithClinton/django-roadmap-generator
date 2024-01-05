from django.shortcuts import render
from decouple import config, Csv
from openai import OpenAI
from django.http import JsonResponse
from .models import Course, Schedule, MiniSchedule
import json
client = OpenAI(api_key=config("OPENAI_API_KEY"),)

# Create your views here.
def index(request):
    courses = Course.objects.all()
    if request.method == 'POST':
        data = json.loads(request.body)
        prompt_data = data["key1"]
        completion = client.chat.completions.create(
            model="gpt-3.5-turbo-1106",
            response_format={ "type": "json_object" },
            messages=[
                {"role": "system", "content": "You are a helpful assistant designed to output JSON."},
                {"role": "user", "content": f"{prompt_data}"}
            ]
            )

        print(completion.choices[0].message.content) 
        new_output = completion.choices[0].message.content
        # response['choices'][0]['message']['content']
        return JsonResponse(new_output, safe=False)
        
    context = {"courses": courses}
    return render(request, "courses/index.html", context)


def detail(request, slug):
    course = Course.objects.get(slug=slug)
    schedules = Schedule.objects.all()
    context = {"course":course, "schedules": schedules}
    return render(request, "courses/detail.html", context)

def ask_openai(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        course_id = data["c_id"]
        schedule_id = data["sch_id"]
        mini_schedule_id = data["mini_sch_id"]
        
        course_label = Course.objects.get(id=course_id).label
        schedule = Schedule.objects.get(id=schedule_id)
        mini_schedule = MiniSchedule.objects.get(id=mini_schedule_id)
        
        print(course_label)
        print(schedule)
        print(mini_schedule)
        
        print(f"{course_label} roadmap for {mini_schedule} {schedule}")
        
        completion = client.chat.completions.create(
            model="gpt-3.5-turbo-1106",
            response_format={ "type": "json_object" },
            messages=[
                {"role": "system", "content": f"""
                 
                 You are a helpful assistant designed to output JSON, 
                 JSON output should contain title, 
                 duration, frequency, learning_roadmap. learning_roadmap should be an array of comprehensive topics to learn
                 """
                 },
                {"role": "user", "content": f"comprehensive {course_label} roadmap for {mini_schedule} {schedule} every {schedule}"}
            ]
            )

        print(completion.choices[0].message.content) 
        new_output = completion.choices[0].message.content
        
        return JsonResponse(new_output, safe=False)
    
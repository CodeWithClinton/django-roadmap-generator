from django.shortcuts import render
from decouple import config, Csv
from openai import OpenAI
from django.http import JsonResponse
from .models import Course, Schedule
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
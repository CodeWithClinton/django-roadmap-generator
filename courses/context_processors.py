from .models import Course

def course_context(request):
    roadmaps = Course.objects.all()
    return {
        "roadmaps":roadmaps
    }
from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Course, Schedule, MiniSchedule, Roadmap, UserCourse, Quiz, QuizOption


# Register your models here.
class CourseAdmin(SummernoteModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    summernote_fields = ('description',)
    
    
admin.site.register(Course, CourseAdmin)
admin.site.register(Schedule)
admin.site.register(MiniSchedule)
admin.site.register(UserCourse)
admin.site.register(Roadmap)
admin.site.register(Quiz)
admin.site.register(QuizOption)

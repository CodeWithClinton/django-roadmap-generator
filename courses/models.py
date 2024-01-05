from django.db import models
from django.conf import settings

# Create your models here.
class Course(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField()
    description = models.TextField()
    thumbnail = models.ImageField(upload_to="img")
    label = models.CharField(max_length=25, blank=True, null=True)
    
    def __str__(self):
        return self.title


class Schedule(models.Model):
    title = models.CharField(max_length=25)
    course = models.ManyToManyField(Course, blank=True)
    
    def __str__(self):
        return self.title 
    
    
class MiniSchedule(models.Model):
    title = models.CharField(max_length=25)
    schedule =models.ForeignKey(Schedule, on_delete=models.CASCADE, related_name="mini_schedule")
    
    def __str__(self):
        return self.title
    


class Roadmap(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="roadmap")
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="roadmap")
    title = models.CharField(max_length=25, blank=True, null=True)
    schedule = models.ForeignKey(Schedule, on_delete=models.CASCADE, related_name="roadmap", blank=True, null=True)
    mini_schedule = models.ForeignKey(MiniSchedule, on_delete=models.CASCADE, related_name="roadmap", blank=True, null=True)
    
    def __str__(self):
        return f"{self.user.username} - {self.course.title}"
    
from django.db import models

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
    
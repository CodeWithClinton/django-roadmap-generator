from django.db import models
from django.conf import settings

# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=20)
    
    def __str__(self):
        return self.title


class Course(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField()
    description = models.TextField()
    thumbnail = models.ImageField(upload_to="img")
    label = models.CharField(max_length=25, blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    
    def __str__(self):
        return self.title



class CourseAlert(models.Model):
    email = models.EmailField()
    
    def __str__(self):
        return self.email

class Schedule(models.Model):
    title = models.CharField(max_length=25)
    
    def __str__(self):
        return self.title 
    
        
class MiniSchedule(models.Model):
    title = models.CharField(max_length=25)
    schedule =models.ForeignKey(Schedule, on_delete=models.CASCADE, related_name="mini_schedule")
    
    def __str__(self):
        return self.title
    



class UserCourse(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="user_course")
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="user_course", blank=True, null=True)
    schedule = models.ForeignKey(Schedule, on_delete=models.CASCADE, related_name="user_course", blank=True, null=True)
    mini_schedule = models.ForeignKey(MiniSchedule, on_delete=models.CASCADE, related_name="user_course", blank=True, null=True)
    
    def __str__(self):
        return f"{self.user.username} -- {self.course.title}"
    
    

class Roadmap(models.Model):
    title = models.CharField(max_length=25, blank=True, null=True)
    user_course = models.ForeignKey(UserCourse, on_delete=models.CASCADE, related_name="roadmap", blank=True, null=True)
    
    def __str__(self):
        return f"{self.user_course.course.title} - {self.title}"
  
    
class Quiz(models.Model):
    question = models.CharField(max_length=100)
    user_course = models.ForeignKey(UserCourse, on_delete=models.CASCADE, related_name="quiz", blank=True, null=True)
    answer = models.CharField(max_length=50)
    
    def __str__(self):
        return f"{self.user_course.course.title} - {self.question}"
    
    

class QuizOption(models.Model):
    option = models.CharField(max_length=25)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name="options")
    
    def __str__(self):
        return f"{self.quiz.question} - {self.option}"
    

class UserScore(models.Model): 
    score = models.IntegerField(default=0)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="score")
    user_course = models.ForeignKey(UserCourse, on_delete=models.CASCADE)
    created = models.DateField(auto_now_add=True, blank=True, null=True)
    updated = models.DateField(auto_now=True, blank=True, null=True)
    
    def __str__(self):
        return f"{self.user.username} - {self.user_course.course.title} - {self.score}"
    
    
    
    


    
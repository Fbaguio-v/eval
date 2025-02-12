from django.db import models

# Create your models here.
class Role(models.TextChoices):
    ADMIN = 'Admin', 'Admin'
    COORDINATOR = 'Coordinator', 'Coordinator'
    DEAN = 'Dean', 'Dean'
    STUDENT = 'Student', 'Student'
    FACULTY = 'Faculty', 'Faculty'
class Evaluation(models.Model):
    institute = models.CharField(max_length = 200 )
    profName = models.CharField(max_length = 200)
    created_at = models.DateTimeField(auto_now_add = True)


from django.db import models
from django.contrib.auth.models import User

# Create your models here
class Project(models.Model):
    name=models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    start_date=models.DateField()
    end_date=models.DateField(blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    STATUS_CHO=[
        ('In_progress', 'In Progress'),
        ('Completed', 'Completed'),
        ('On_hold', 'On Hold'),
    ]
    
    
    status= models.CharField(max_length=30, choices=STATUS_CHO, default='in_progress')

    def __str__(self):
        return self.name

class Task(models.Model):
    STATUS_CHOICES=[
        ("Not_Started", "Not Started"),
        ("In_Progress", "In Progress"),
        ("Completed", "Completed"),
    ]

    name=models.CharField(max_length=255)
    description=models.TextField(blank=True)

    status=models.CharField(max_length=20, choices=STATUS_CHOICES, default="Not_Started")
    start_date=models.DateField()
    end_date=models.DateField(blank=True, null=True)
    project=models.ForeignKey(Project, on_delete=models.CASCADE, related_name="tasks")
    # assigned_to =models.ForeignKey()

    def __str__(self):
        return self.name


class Tasklog(models.Model):
    
    task=models.ForeignKey(Task, on_delete=models.CASCADE, related_name="logs")
    msg=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True) # log time
    def __str__(self):
        return f"Log for {self.task.name}"


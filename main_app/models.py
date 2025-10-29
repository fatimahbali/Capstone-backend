from django.db import models

# Create your models here
class Project(models.Model):
    name=models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    start_date=models.DateField()
    end_date=models.DateField(blank=True, null=True)

    STATUS_CHO=[
        ('In_progress', 'In Progress'),
        ('Completed', 'Completed'),
        ('On_hold', 'On Hold'),
    ]
    
    status= models.CharField(max_length=30, choices=STATUS_CHO, default='in_progress')

    def __str__(self):
        return self.name
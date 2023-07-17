from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Project(models.Model):
    title = models.CharField(max_length=64)
    description = models.CharField(max_length=256)

    def __str__(self):
        return self.title

class Issue(models.Model):
    title = models.CharField(max_length=64)
    description = models.CharField(max_length=256)
    date_created = models.DateTimeField("date created")
    STATUS = [
        ("P", "Pending"),
        ("I", "In Progress"),
        ("C", "Completed"),
    ]
    status = models.CharField(max_length=1, choices=STATUS)
    TYPE = [
        ("B", "Bug"),
        ("F", "Feature"),
        ("T", "Task"),
    ]
    type = models.CharField(max_length=1, choices=TYPE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, related_name='created_by', on_delete=models.DO_NOTHING)
    assigned_to = models.ForeignKey(User, related_name='assigned_to', on_delete=models.DO_NOTHING, null=True)
 

    def __str__(self):
        return self.title
    

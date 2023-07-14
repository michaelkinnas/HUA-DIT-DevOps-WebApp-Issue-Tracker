from django.db import models

# Create your models here.
class Issue(models.Model):
    title = models.CharField(max_length=64)
    details = models.CharField(max_length=256)
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

    def __str__(self):
        return self.title
from django.db import models

# Create your models here.

class Meeting(models.Model):
    title  = models.CharField(max_length=100)
    date = models.DateField()
    
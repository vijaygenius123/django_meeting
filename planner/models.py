from django.db import models
from datetime import datetime
# Create your models here.

class Meeting(models.Model):
    title  = models.CharField(max_length=100)
    date = models.DateField()
    start_time = models.TimeField(default=datetime.now)
    duration = models.IntegerField(default=15)

from django.db import models
from datetime import time


# Create your models here.

class Room(models.Model):
    name = models.CharField(max_length=25, default="GOLOKA")
    room_no = models.IntegerField()
    floor = models.IntegerField()

    def __str__(self):
        return f'{self.name} : {self.room_no} is located on {self.floor}'


class Meeting(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateField()
    start_time = models.TimeField(default=time(9))  # adding time using Python for timefield
    duration = models.IntegerField(default=1)  # adding integer for integerfield
    room = models.ForeignKey(Room, on_delete=models.CASCADE) # make sure CASCADE not used as a function

    def __str__(self):
        return f'{self.title} scheduled on {self.date} at {self.start_time}'

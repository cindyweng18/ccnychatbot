from django.db import models
from django.utils import timezone


# Create your models here.

# Room Schema
class Room (models.Model):
    room = models.CharField (max_length = 100)              # Chat room name

    def __str__ (self):
        return self.room

class Message (models.Model):
    value = models.CharField (max_length = 1000000)             # message can have a length of 1 million characters
    date = models.DateTimeField (default = timezone.now(), null = False, blank = True)      # get the current time the message was sent
    user = models.CharField (max_length = 100)                  # name of the user who sent the message
    room = models.ForeignKey (Room, on_delete = models.CASCADE, null=False) # room is a foreign key here and if the room is deleted any messages in that room will simultaneously be deleted

    def __str__ (self):
        return f"Value: {self.value}\tDate: {self.date}\tUser: {self.user}\tRoom: {self.room}"

    
    
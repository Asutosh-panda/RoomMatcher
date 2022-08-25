
from django.db import models
from hostel.models import Hostelite,Register
from room.models import Room
# Create your models here.

class SelectMatch(models.Model):
    sic = models.ForeignKey(Register,on_delete=models.CASCADE)
    later = models.IntegerField()
    status1  = models.BooleanField(default=False)
    status2 = models.BooleanField(default=False)
    def __str__(self):
        return str(self.sic)


class Match(models.Model):
    roomate1 = models.IntegerField()
    roomate2 = models.IntegerField()
    room_no = models.ForeignKey(Room,on_delete=models.CASCADE)


    def __str__(self):
        return str(self.room)   

from django.db import models
from hostel.models import Hostelite,Register
from room.models import Room
# Create your models here.
class SelectMatch(models.Model):
    sic = models.ForeignKey(Register,on_delete=models.CASCADE)
    later = models.IntegerField()

    def __str__(self):
        return str(self.sic)


class Match(models.Model):
    roomate1 = models.CharField(max_length=20)
    roomate2 = models.CharField(max_length=20)
    room = models.ForeignKey(Room,on_delete=models.DO_NOTHING)

    def __str__(self):
        return str(self.room)   
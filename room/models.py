from django.db import models

# Create your models here.
class Room(models.Model):
    room_no = models.IntegerField(primary_key=True)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return str(self.room_no)
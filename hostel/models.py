from django.db import models
import datetime
from django.contrib.auth.models import User

def year_choices():
    return [(r,r) for r in range(current_year()-4, datetime.date.today().year+1)]


def current_year():
    return datetime.date.today().year
# Create your models here.

class Hostelite(models.Model):
    choices = [("M","Male"),("F","Female"),]
    branches = [("CS","CSE"),("E","ECE"),("EE","EEE"),("EI","EIE")]
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=30)
    gender = models.CharField(max_length=10,choices=choices,default="M")
    branch = models.CharField(max_length=5,choices=branches,default="CS")
    home = models.CharField(max_length=15)
    sic = models.IntegerField(primary_key=True)
    year = models.IntegerField(choices=year_choices(), default=current_year())
    enroll_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return str(self.sic)
    

class Register(models.Model):
    
    sic = models.ForeignKey(Hostelite,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    desc = models.TextField()
    hobby = models.CharField(max_length=100)

    def __str__(self):
        return str(self.sic)
    
    

class Action(models.Model):
    sic = models.ForeignKey(User,on_delete=models.CASCADE)
    rc = models.BooleanField(default=False)
    dc = models.BooleanField(default=False)



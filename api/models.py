from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class Advisor(models.Model):
    name = models.CharField(max_length=50, unique=True)
    photo = models.ImageField(upload_to="advisors" )

class User(AbstractUser):
    name = models.CharField(max_length=50, null=False, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=200)

class Book_advisor(models.Model):
    advisor = models.ForeignKey(Advisor, on_delete=models.CASCADE)
    booking_time = models.DateTimeField(auto_now=False)
    
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    us_studen = models.BooleanField()
    is_teacher = models.BooleanField()

    def __str__(self):
        return self.username


class Student(models.Model):
    user = models.OneToOneField(User,on_delete= models.CASCADE)


    def __str__(self):
        return self.user.username 

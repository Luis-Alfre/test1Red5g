from pyexpat import model
from django.db import models
from django.contrib.auth.models import AbstractUser

class User(models.Model):
    name =  models.CharField(max_length=70)
    mail = models.EmailField()
    password = models.CharField(max_length=20)
    direction = models.CharField(max_length=50)
    phone = models.CharField(max_length=30)
    date = models.DateField()
    
    
    
# class User(AbstractUser):
#     email = models.EmailField(
#         max_length=150, unique=True)
#     REQUIRED_FIELDS = ['username', 'password']  # new

   
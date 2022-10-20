from django.db import models

class User(models.Model):
    name =  models.CharField(max_length=70)
    mail = models.EmailField()
    password = models.CharField(max_length=20)
    direction = models.CharField(max_length=50)
    phone = models.CharField(max_length=30)
    date = models.DateField()
    
    
    

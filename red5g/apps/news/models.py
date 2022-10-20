from turtle import title
from django.db import models

class News(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    
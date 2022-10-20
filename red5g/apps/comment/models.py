from django.db import models

from apps.news.models import News

class Comment(models.Model):
    description = models.CharField(max_length=100)
    news = models.ForeignKey(News, related_name='news', on_delete=models.CASCADE)

from rest_framework import serializers

from apps.news.models import News
from apps.comment.models import Comment

class commentSerializer(serializers.ModelSerializer):
    news = News
    
    class Meta:
        model = Comment
        fields = ['description','news']   
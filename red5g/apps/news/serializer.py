
from rest_framework import serializers

from apps.news.models import News

class newsSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = News
        fields = "__all__"    
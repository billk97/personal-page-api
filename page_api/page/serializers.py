from rest_framework import serializers

from .models import Article


class ArticleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Article
        fields = ('id', 'title', 'thumbnail_path_text', 'html_text', 'created_date', 'minutes_to_read')

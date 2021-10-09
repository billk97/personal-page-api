import json

from django.http import JsonResponse, HttpResponse
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.decorators import api_view

from .models import Article
from .serializers import ArticleSerializer
from django.core import serializers


# @api_view(["GET"])
# def get_articles(request):
#     articles = Article.objects.all()
#     serializer = ArticleSerializer(articles, many=True)
#     return JsonResponse({'articles': serializer.data}, safe=False, status=status.HTTP_200_OK)


@api_view(["GET"])
def get_article(request, article_id):
    article = Article.objects.get(pk=article_id)
    serializer = ArticleSerializer(article)
    return JsonResponse({'article': serializer.data})


# @api_view(["POST"])
# def add_article(request, article):
#     article = Article(article.title, article.thumbnail_path_text, article.html_text, article.description, article.minutes_to_read)
#     article.save()
#     serializer = ArticleSerializer(article)
#     return JsonResponse({'article': serializer.data})


class ArticleView(View):

    def get(self, request, *args, **kwargs):
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)
        return JsonResponse({'articles': serializer.data}, safe=False, status=status.HTTP_200_OK)

    @csrf_exempt
    def post(self, request, *args, **kwargs):
        data = json.loads(request.body)
        print(data)
        article = Article.objects.create(
            title=data.get('title'),
            thumbnail_path_text=data.get('thumbnail_path_text'),
            html_text=data.get('html_text'),
            description=data.get('description'),
            minutes_to_read=data.get('minutes_to_read')
        )
        article.save()
        return JsonResponse('ok', status=status.HTTP_200_OK, safe=False)
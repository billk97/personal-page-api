from django.shortcuts import render
from django.http import HttpResponse
from .models import Article
from rest_framework import viewsets
from .serializers import ArticleSerializer


# def index(request):
#     return HttpResponse("Test")


# def articles(request):
#     return HttpResponse(Article.objects.all())


class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all().order_by('id')
    serializer_class = ArticleSerializer

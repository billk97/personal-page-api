from django.conf.urls import url
from django.urls import path
from . import views


urlpatterns = [
    path('articles', views.ArticleView.as_view()),
    path('articles/<int:article_id>', views.get_article),
]
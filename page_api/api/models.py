from django.db import models
from django.utils import timezone
import datetime


class Article(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255, null=False)
    thumbnail_path_text = models.CharField(max_length=255)
    html_text = models.TextField()
    description = models.CharField(max_length=255)
    created_date = models.DateTimeField(auto_now_add=True)
    minutes_to_read = models.IntegerField(default=0)

    def __str__(self):
        return '{ id: %d, title: %s }' % (self.id, self.title)

    def is_new(self):
        return self.created_date >= timezone.now() - datetime.timedelta(weeks=1)

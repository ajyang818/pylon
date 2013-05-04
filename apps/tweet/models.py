from django.db import models

# Create your models here.


class Tweet(models.Model):

    author = models.CharField(max_length=50)
    content = models.CharField(max_length=180)
    date_published = models.DateTimeField(auto_now=True)

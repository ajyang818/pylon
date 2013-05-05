from django.db import models

# Create your models here.


class Author(models.Model):

    author_id = models.BigIntegerField()
    screen_name = models.CharField(max_length=40, blank=True, null=True)
    author_name = models.CharField(max_length=50, blank=True, null=True)
    author_created = models.DateTimeField(blank=True, null=True)
    author_description = models.CharField(max_length=500, blank=True, null=True)

    def __unicode__(self):
        return self.screen_name


class Hashtag(models.Model):

    hashtag = models.CharField(max_length=50)


class Tweet(models.Model):

    author = models.ForeignKey(Author)
    tweet_id = models.BigIntegerField()
    content = models.CharField(max_length=180)
    date_published = models.DateTimeField(auto_now=True)

    coordinates = models.CharField(max_length=100, null=True, blank=True)
    user_mentions = models.CharField(max_length=200, null=True, blank=True)

    hashtags = models.ManyToManyField(Hashtag, null=True, blank=True)

    def __unicode__(self):
        return self.content

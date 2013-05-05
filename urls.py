from django.conf.urls import patterns, url
from django.contrib import admin

from tweet.views import HomeView, LoggedInSuccessView, LogOutView, GetTweetsByUserView

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', HomeView.as_view(), name="home"),
    url(r'^loggedin/$', LoggedInSuccessView.as_view(), name="logged_in_success"),
    url(r'^logout/$', LogOutView.as_view(), name='log_out'),
    url(r'^gettweets/user/$', GetTweetsByUserView.as_view(), name="get_tweets_user"),
)

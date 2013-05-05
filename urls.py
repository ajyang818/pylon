from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib import admin
from django.views.generic import TemplateView
from django.views.generic.base import RedirectView

from tweet.views import HomeView, LoggedInSuccessView, LogOutView

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', HomeView.as_view(), name="home"),
    url(r'^loggedin/$', LoggedInSuccessView.as_view(), name="logged_in_success"),
    url(r'^logout/$',LogOutView.as_view(),name='log_out'),
)
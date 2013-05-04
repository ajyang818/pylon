# Create your views here.

from django.shortcuts import render
from django.views.generic.base import TemplateView

from twython import Twython

APP_KEY = 'GVu8UN13fVaVayJ02yvrA'
APP_SECRET = 'BztuG3PbMdMCwVbSExFgdYtoN4zonDkeYPbFd9qFjp4'


class HomeView(TemplateView):

    def get(self, request):
        twitter_link = self.link_to_twitter(request)
        context = {
            'body': 'Hello Dan',
            'twitter_link': twitter_link,
        }
        template = "home.html"
        return render(request, template, context)

    def link_to_twitter(self, request):

        t = Twython(APP_KEY, APP_SECRET)

        authentication_props = t.get_authentication_tokens(callback_url='http://localhost:8000/loggedin')

        # request.session['oauth_token'] = auth_props['oauth_token']
        request.session['oauth_token_secret'] = authentication_props['oauth_token_secret']

        return authentication_props['auth_url']


class LoggedInSuccessView(TemplateView):

    def get(self, request, *args, **kwargs):

        oauth_token = request.GET.get('oauth_token')
        oauth_verifier = request.GET.get('oauth_verifier')

        oauth_token_secret = request.session['oauth_token_secret']

        t = Twython(APP_KEY, APP_SECRET, oauth_token, oauth_token_secret)

        # Authentication vs. authorization is confusing; following variables should be renamed
        # to make it all clearer
        auth_tokens = t.get_authorized_tokens(oauth_verifier)

        oauth_token = auth_tokens['oauth_token']
        oauth_token_secret = auth_tokens['oauth_token_secret']

        t2 = Twython(APP_KEY, APP_SECRET, oauth_token, oauth_token_secret)

        home_timeline = t2.getHomeTimeline()

        context = {
            'auth_tokens': auth_tokens,
            'home_timeline': home_timeline,
        }
        template = "logged_in_success.html"
        return render(request, template, context)

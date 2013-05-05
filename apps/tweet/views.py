from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView
import settings.settings as settings

from twython import Twython

from tweet.forms import GetTweetsByUserForm
from tweet.utils import get_tweets_by_user


class HomeView(TemplateView):

    def get(self, request):
        if('authorization_token' not in request.session.keys()):
            twitter_link = self.link_to_twitter(request)
            context = {
                'body': 'Hello Dan',
                'twitter_link': twitter_link,
            }
            template = "home.html"
            return render(request, template, context)
        # else
        oauth_token = request.session['authorization_token']
        oauth_token_secret = request.session['authorization_token_secret']

        t2 = Twython(settings.APP_KEY, settings.APP_SECRET, oauth_token, oauth_token_secret)

        home_timeline = t2.getHomeTimeline()

        context = {
            'auth_tokens': {'oauth_token': oauth_token, 'oauth_token_secret': oauth_token_secret},
            'home_timeline': home_timeline,
        }
        template = "logged_in_success.html"
        return render(request, template, context)

    def link_to_twitter(self, request):

        t = Twython(settings.APP_KEY, settings.APP_SECRET)

        authentication_props = t.get_authentication_tokens(callback_url=settings.LOGIN_CALLBACK_URL)

        # request.session['oauth_token'] = auth_props['oauth_token']
        request.session['oauth_token_secret'] = authentication_props['oauth_token_secret']

        return authentication_props['auth_url']


class LogOutView(TemplateView):

    def get(self, request, *args, **kwargs):
        request.session.clear()
        return redirect('/')


class LoggedInSuccessView(TemplateView):

    def get(self, request, *args, **kwargs):

        if('authorization_token' not in request.session.keys()):

            if('oauth_token' not in request.GET or 'oauth_verifier' not in request.GET):
                return redirect('/')

            oauth_token = request.GET.get('oauth_token')
            oauth_verifier = request.GET.get('oauth_verifier')

            oauth_token_secret = request.session['oauth_token_secret']

            t = Twython(settings.APP_KEY, settings.APP_SECRET, oauth_token, oauth_token_secret)

            authorization_tokens = t.get_authorized_tokens(oauth_verifier)

            request.session['authorization_token'] = authorization_tokens['oauth_token']
            request.session['authorization_token_secret'] = authorization_tokens['oauth_token_secret']

        return redirect('/')


class GetTweetsByUserView(TemplateView):

    def get(self, request):
        form = GetTweetsByUserForm()
        template = "get_tweets_user.html"
        context = {
            'form': form,
        }
        return render(request, template, context)

    def post(self, request, *args, **kwargs):
        # username_to_get = self.form.save(self.request.user)
        username_to_get = self.request.POST.get('twitter_username')
        get_tweets_by_user(request=request, username=username_to_get)
        return HttpResponse(redirect('get_tweets_user'))

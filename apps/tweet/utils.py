import datetime
import settings.settings as settings

from twython import Twython

from tweet.models import Author, Tweet


def get_tweets_by_user(request, username):
    oauth_token = request.session['authorization_token']
    oauth_token_secret = request.session['authorization_token_secret']

    twython = Twython(settings.APP_KEY, settings.APP_SECRET, oauth_token, oauth_token_secret)

    raw_tweets = twython.getUserTimeline(screen_name=username, count=20)

    return save_tweets(raw_tweets)


def save_tweets(raw_tweets):
    tweets_author = raw_tweets[0]['user']
    tweets_author_id = tweets_author['id']
    author_kwargs = {
        'screen_name': tweets_author.get('screen_name'),
        'author_name': tweets_author.get('name'),
        # Stupid datetime...need to figure out how to parse
        # 'author_created': tweets_author.get('created_at'),
        'author_description': tweets_author.get('description')
    }
    author, created = Author.objects.get_or_create(author_id=tweets_author_id,
                                                    **author_kwargs)

    for tweet in raw_tweets:
        tweet_id = tweet['id']
        tweet_kwargs = {
            'author': author,
            'content': tweet['text'],
            # date_published: tweet['created_at'],
            'date_published': datetime.datetime.now(),
            'coordinates': tweet.get('coordinates'),
            # Hashtags and user_mentinos TO BE IMPLEMENTED
            # 'user_mentions': tweet['entities'].get('user_mentions'),
            # hashtags: TO BE IMPLEMENTED
        }
        our_tweet, created = Tweet.objects.get_or_create(tweet_id=tweet_id,
                                                            **tweet_kwargs)

    return

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
        'author_id': tweets_author_id,
        'screen_name': tweets_author.get('screen_name'),
        'author_name': tweets_author.get('name'),
        # Stupid datetime...need to figure out how to parse
        # 'author_created': tweets_author.get('created_at'),
        'author_description': tweets_author.get('description')
    }
    # TO-DO: Figure out get_or_create on a variable but save with **kwargs
    try:
        author = Author.objects.get(author_id=tweets_author_id)
    except Author.DoesNotExist:
        author = Author(**author_kwargs)
        author.save()

    for tweet in raw_tweets:
        tweet_id = tweet['id']
        tweet_kwargs = {
            'tweet_id': tweet_id,
            'author': author,
            'content': tweet['text'],
            # date_published: tweet['created_at'],
            'date_published': datetime.datetime.now(),
            'coordinates': tweet.get('coordinates'),
            # Hashtags and user_mentinos TO BE IMPLEMENTED
            # 'user_mentions': tweet['entities'].get('user_mentions'),
            # hashtags: TO BE IMPLEMENTED
        }
        try:
            our_tweet = Tweet.objects.get(tweet_id=tweet_id)
        except Tweet.DoesNotExist:
            our_tweet = Tweet(**tweet_kwargs)
            our_tweet.save()

    return

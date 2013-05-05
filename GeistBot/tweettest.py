import twitter

TOKEN = '1405726080-HxcGxqfQLZHxDh6WfMi0SxhxM2T06BgXvIAVqmk'
TOKEN_KEY = 'dLLrJqG4Nv8cCKRbjdUP51zvZLNeoejZ5YlhJNV8fI'
CON_SEC = 'XBtHrvyFAQS8GMzZzFvFgw'
CON_SEC_KEY = 'H167uWb9azWBoXrrE0uCcKWZm2nY9MbsWY0ngg45s'

my_auth = twitter.OAuth(TOKEN,TOKEN_KEY,CON_SEC,CON_SEC_KEY)
twit = twitter.Twitter(auth=my_auth)
twit.statuses.update(status="Hello, World.")
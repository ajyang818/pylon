import tweetstream
import twitter
import datetime

import re
from nltk.corpus import stopwords
from collections import Counter

def send_tweet(message):
	TOKEN = '1405726080-HxcGxqfQLZHxDh6WfMi0SxhxM2T06BgXvIAVqmk'
	TOKEN_KEY = 'dLLrJqG4Nv8cCKRbjdUP51zvZLNeoejZ5YlhJNV8fI'
	CON_SEC = 'XBtHrvyFAQS8GMzZzFvFgw'
	CON_SEC_KEY = 'H167uWb9azWBoXrrE0uCcKWZm2nY9MbsWY0ngg45s'

	my_auth = twitter.OAuth(TOKEN,TOKEN_KEY,CON_SEC,CON_SEC_KEY)
	twit = twitter.Twitter(auth=my_auth)

	# generate message using digest()
	twit.statuses.update(status=message)

def digest(data):
	# data
	with open ("tweets/tweets.csv", "r") as myfile:
	    data=myfile.read().replace('\n', ' ')

	#We only want to work with lowercase for the comparisons
	data = data.lower()
	datalist = data.split()

	# keeps hashtags, @users, or words - apostrophes ok
	datalist = [i for i in datalist if re.match("^[@#]?\w+'?\w+$", i)]

	# drops stop words
	datalist = [i for i in datalist if i not in stopwords.words('english')]

	# print important_words
	counterObj = Counter()
	counterObj.update(datalist)

	# sort by frequency to get list of key, value : term, freq
	freqlist = counterObj.most_common()

	message = ""
	for key,value in freqlist:
		message = 

digest("ipsum lorem")
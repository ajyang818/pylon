import tweetstream
import twitter
import datetime

import re
from nltk.corpus import stopwords
from collections import Counter

stream = tweetstream.SampleStream("GeistBot", "vi23EnuBv")
for tweet in stream:

	try:
		print tweet["text"]
	except:
		continue
	print '\n'
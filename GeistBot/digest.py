import re
from nltk.corpus import stopwords
from collections import Counter

# data = '29 gold, 17 silver, 19 bronze - We finished 3rd in medal table after most successful Olympics for 104 years #OurGreatestTeam RT your support'
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
print counterObj.most_common()
from __future__ import absolute_import, print_function

import nltk, matplotlib
import json

from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

#Access keys for Twitter API
consumer_key="8HWEs4jn3xtACLsGIWLYUpQPk"
consumer_secret="psCQLSvzknEqO3t1RNUSAySYza97Kiqq19kyqmCP6c2NCyvIqQ"
access_token="561611360-UqcM5EUcireTX13YlW56F6oaPlkYgMk7ixTvAvvy"
access_token_secret="CpUApbuhJdE2CLxt8RnABLWKaHXZbps5dB4DtVBGdHYIt"

class StdOutListener(StreamListener):

    # only look at the tweet's text itself, tokenize it as we read in tweets
    def on_data(self, data):
        text = (json.loads(data)['text'])
        text = (nltk.word_tokenize(text))
        print(text)
        return True

    def on_error(self, status):
        print(status)

if __name__ == '__main__':
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    stream = Stream(auth, l)

    #looking for tweets with hashtags denoting sarcasm
    stream.filter(track=['#sarcasm', '#sarcastic'])

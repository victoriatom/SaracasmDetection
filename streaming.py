from __future__ import absolute_import, print_function
import json

from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

# Go to http://apps.twitter.com and create an app.
# The consumer key and secret will be generated for you after
consumer_key="8HWEs4jn3xtACLsGIWLYUpQPk"
consumer_secret="psCQLSvzknEqO3t1RNUSAySYza97Kiqq19kyqmCP6c2NCyvIqQ"

# After the step above, you will be redirected to your app's page.
# Create an access token under the the "Your access token" section
access_token="561611360-UqcM5EUcireTX13YlW56F6oaPlkYgMk7ixTvAvvy"
access_token_secret="CpUApbuhJdE2CLxt8RnABLWKaHXZbps5dB4DtVBGdHYIt"

class StdOutListener(StreamListener):
    """ A listener handles tweets that are received from the stream.
    This is a basic listener that just prints received tweets to stdout.
    """
    def on_data(self, data):
        print(json.loads(data)['text'])
        return True

    def on_error(self, status):
        print(status)


if __name__ == '__main__':
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    stream = Stream(auth, l)
    stream.filter(track=['sarcasm'])

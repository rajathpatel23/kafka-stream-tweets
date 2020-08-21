from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from kafka import KafkaProducer
import os

access_token = os.environ.get("TWEET_ACCESS_TOKEN")
access_token_secret = os.environ.get("TWEET_ACCESS_SECRET")
consumer_key = os.environ.get("TWEET_CONSUMER_KEY")
consumer_secret = os.environ.get("TWEET_CONSUMER_SECRET")


class StdOutListener(StreamListener):
    def on_data(self, data):
        producer.send("msdhoni", data.encode('utf-8'))
        return True
    def on_error(self, status):
        print (status)


if __name__ == '__main__':
    producer = KafkaProducer(bootstrap_servers=['localhost:9092'])
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)
    stream.filter(track="msdhoni")
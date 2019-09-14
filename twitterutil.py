import re
import tweepy
from tweepy import OAuthHandler
from textblob import TextBlob
import datetime


class TwitterClient(object):

    no_of_page = 2

    def __init__(self):
        consumer_key = '0jVPjPQCAKL7oWB1ffnQRKncM'
        consumer_secret = 'd7CfgN5UDyctKsd5ZksuiwI2kyzzMJHatlSYBsahqRddQctVyO'
        access_token = '961245627198849025-HRpNwqafMJVcwNBv8VL49xt0LZRz2uj'
        access_token_secret = 'Wt6jhKri40DrposBZ5p3b3jX3de2C1ofpV0pA3bNgKGC4'

        try:
            self.auth = OAuthHandler(consumer_key, consumer_secret)
            self.auth.set_access_token(access_token, access_token_secret)
            self.api = tweepy.API(self.auth)

        except:
            print("Error: Authentication Failed")

    def clean_tweet(self, tweet):
        '''
        Utility function to clean tweet text by removing links, special characters
        using simple regex statements.
        '''
        return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t]) |(\w+:\/\/\S+)", " ", tweet).split())

    def get_tweet_sentiment(self, tweet):
        analysis = TextBlob(self.clean_tweet(tweet))
        return analysis

    def get_tweets(self, username, start, end):
        page = 1
        slist = [int(x) for x in str(start).split('-')]
        elist = [int(x) for x in str(end).split('-')]
        startDate = datetime.datetime(slist[0], slist[1], slist[2], 0, 0, 0)
        endDate = datetime.datetime(elist[0], elist[1], elist[2], 0, 0, 0)
        ret_tweets = []
        print ('While started...')
        while page <= self.no_of_page:
            tweets = self.api.user_timeline(username, page=page)
            print('Page No : ', page)
            print('Collected :', len(ret_tweets))
            for tweet in tweets:
                if tweet.created_at <= endDate and tweet.created_at >= startDate:
                    ret_tweets.append(tweet)
            page += 1
        return self.get_parsed_tweets(ret_tweets)

    def get_parsed_tweets(self, intweets):
        tweets = []
        for tweet in intweets:
            parsed_tweet = dict()
            parsed_tweet['sentiment'] = self.get_tweet_sentiment(tweet.text).polarity
            parsed_tweet['subjectivity'] = self.get_tweet_sentiment(tweet.text).subjectivity
            parsed_tweet['Date'] = tweet.created_at.strftime('%Y-%m-%d')
            if tweet.retweet_count > 0:
                if parsed_tweet not in tweets:
                    tweets.append(parsed_tweet)
            else:
                tweets.append(parsed_tweet)
        return tweets
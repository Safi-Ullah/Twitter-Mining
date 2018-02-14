import tweepy

class TweetReader:

    def __init__(self):
        self.__consumer_key = "Your Consumer Key"
        self.__consumer_secret = "Your Consumer Secret"
        self.__access_token = "Your Access Token"
        self.__access_token_secret = "Your Access Token Secret"
        self.auth = None
        self.api = None

    def authorize_connection(self):
        self.auth = tweepy.OAuthHandler(self.__consumer_key, self.__consumer_secret)
        self.auth.set_access_token(self.__access_token, self.__access_token_secret)
        self.api = tweepy.API(self.auth)

    def read_public_tweets(self):
        public_tweets = self.api.home_timeline()

        for tweet in public_tweets:
            yield tweet.text
        return

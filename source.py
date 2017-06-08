from tweet_reader import TweetReader
from tweet_parser import TweetParser

if __name__ == "__main__":
    reader = TweetReader()
    reader.authorize_connection()
    tweet_generator = reader.read_public_tweets()

    parser = TweetParser()

    for i in range(0, 20):
        tweet = next(tweet_generator)
        print (tweet)
        for tag in parser.parse(tweet):
            file.write(tag + "\t")
        file.write("\n")
        print ("-----------------------------------------------------")

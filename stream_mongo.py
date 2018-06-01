#the below saves tweets to the mongo database

from tweepy import Stream
from tweepy.streaming import StreamListener
from auth import get_auth
from pymongo import MongoClient
import json

MONGODB_URI = "mongodb://user:password@ds137550.mlab.com:37550/try_mongo_tweets"
MONGODB_NAME = "try_mongo_tweets"

keyword_List=["Michael"]
limit = 1


class MyStreamListener(StreamListener):
    
    def __init__(self):
        super(MyStreamListener, self).__init__()
        self.num_tweets = 0
        
    def on_data(self, data):
        if self.num_tweets < limit:
            self.num_tweets += 1
            try:
                with MongoClient(MONGODB_URI) as conn:
                    db = conn[MONGODB_NAME]
                    #db above is just a variable name nothing to do with database
                    #the below references the tweets collection
                    coll = db["tweets"]
                    #the below inserts tweets into the tweets collection
                    coll.insert(json.loads(data))
                    return True
            except BaseException as e:
                print("Failed on_data: %s" % str(e))
            return True
        else:
            return False
            
    def on_error(self, status):
        print(status)
        return True
        
auth = get_auth()

twitter_stream = Stream(auth, MyStreamListener())
twitter_stream.filter(track=keyword_List)    


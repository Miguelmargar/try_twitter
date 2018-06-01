from pymongo import MongoClient

MONGODB_URI = "mongodb://User:password@ds137550.mlab.com:37550/try_mongo_tweets"
MONGODB_NAME = "try_mongo_tweets"

buster = {
    "breed": "jack russell",
    "color": "black and tan",
    "gender": "male",
    "name": "buster"
}

with MongoClient(MONGODB_URI) as conn:
    db = conn[MONGODB_NAME]
    #db above is just a variable name nothing to do with database
    #the below references dogs and cats collections
    d = db["dogs"]
    c = db["cats"]
    #the below inserts buster into the dogs collection
    d.insert(buster)   
    
import tweepy
from auth import get_api

api = get_api()

def search(query, count):
    return [status for status in tweepy.Cursor(api.search, q=query).items(count)]

tweets = search("brexit", 10)

#tweets[0] = looks at the first tweet being searched as we are searching for 10 tweets in the line above    
print("Text of tweet: " + tweets[0].text)
print("User's screen name: " + tweets[0].user.screen_name)
#the below loops through the hashtags in order to get the text of each hashtag printed out
hashtags = [h["text"] for h in tweets[0].entities["hashtags"]]
print("Hashtags: " + str(hashtags))
print("User's followers: " + str(tweets[0].user.followers_count))
print("User's friends: " + str(tweets[0].user.friends_count))
print("User's Tweet Count: " + str(tweets[0].user.statuses_count))

usr = round(tweets[0].user.followers_count / first_tweet)
import json
import tweepy
from tweepy import OAuthHandler

CONSUMER_KEY = '2K12xGe8fVhh99GcAoJd7yF7v'
CONSUMER_SECRET = 'Y0y0Z3phHaPbDjvzNkerrH4UhtXWYR4118mifSWPzD6WWO4svO'
OAUTH_TOKEN = '1002151990930149377-QarcQ0KB44YE71qoVWbrkDE9xb2iDZ'
OAUTH_TOKEN_SECRET = 'L8wvks3EiY18AXlwmWmG2gtHbNsIdxGwQLAs5Mv7b4URW'

auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
api = tweepy.API(auth)

#to get the timeline of your own tweets
def get_my_timeline(count):
    return tweepy.Cursor(api.home_timeline).items(count)
    
for status in get_my_timeline(1):
    print(status)
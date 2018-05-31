import json
import tweepy
from tweepy import OAuthHandler

CONSUMER_KEY = '2K12xGe8fVhh99GcAoJd7yF7v'
CONSUMER_SECRET = 'Y0y0Z3phHaPbDjvzNkerrH4UhtXWYR4118mifSWPzD6WWO4svO'
OAUTH_TOKEN = '1002151990930149377-QarcQ0KB44YE71qoVWbrkDE9xb2iDZ'
OAUTH_TOKEN_SECRET = 'L8wvks3EiY18AXlwmWmG2gtHbNsIdxGwQLAs5Mv7b4URW'

#this two functions are the boiler plate lines for the tweepy app so that we don't have to write it all again and just call the function. would need to link other pages to this one as this one is the one that has the consumer and auth tokens.
#the other pages still need to import json and tweepy = this will be done by saying from auth import get_api and create a variable called api = get_api()
def get_auth():
    auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
    return auth    

def get_api():
    auth = get_auth()
    return tweepy.API(auth)
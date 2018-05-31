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

DUB_WOE_ID = 560743
UK_WOE_ID = 23424975


#the below lines can all be compressed into one for each dub and uk with the below:
#set_uk = set([i["name"] for i in api.trends_place(UK_WOE_ID)[0]["trends"]]) - for uk as eg

dub_trends = api.trends_place(DUB_WOE_ID)
uk_trends = api.trends_place(UK_WOE_ID)

trendublin = dub_trends[0]["trends"]
trenduk = uk_trends[0]["trends"]

trend_names_dub = [i["name"] for i in trendublin] 
trend_names_uk = [i["name"] for i in trenduk]

set_dub = set(trend_names_dub)
set_uk = set(trend_names_uk)

#the below gets the areas that are trending in both dub and uk
both = set.intersection(set_dub, set_uk)


print (json.dumps(dub_trends, indent=1))
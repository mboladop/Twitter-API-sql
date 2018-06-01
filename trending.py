import json
import tweepy
from auth import get_api

api = get_api()

DUB_WOE_ID = 560743
UK_WOE_ID = 23424975

dub_trends = api.trends_place(DUB_WOE_ID)
uk_trends = api.trends_place(UK_WOE_ID)



dtrend_set= set([t['name'] for t in dub_trends[0]['trends']])
uktrend_set= set([t['name']for t in uk_trends[0]['trends']])

both = set.intersection(dtrend_set, uktrend_set)

print (both)







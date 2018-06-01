import json
import tweepy
from tweepy import OAuthHandler

CONSUMER_KEY = 'CvQsFoqTEY1s64EJPzQQ87dPz'
CONSUMER_SECRET = '5dGRwepi1y6G3J7DDjhL5mhP9LraTWt7I8QBArSjgfrYSPcgWu'
OAUTH_TOKEN = '160514302-RhZSeqYXYk8FC20DrxvvA0UYPvu2GcGIyG5zSi35'
OAUTH_TOKEN_SECRET = 'U7qq5yNru2VyXHOE5B40n8T6pjdoZWLxPmlh99DDGqxzx'

auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
api = tweepy.API(auth)

def get_auth():
    auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
    return auth    

def get_api():
    auth = get_auth()
    return tweepy.API(auth)
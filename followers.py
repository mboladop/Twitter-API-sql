import tweepy
from auth import get_api

api = get_api()

def get_friends_of(username):
    user = api.get_user(username)
    return user.friends()

friends = get_friends_of("@richardadalton")

for friend in friends:
    print(friend)
import tweepy
from auth import get_api

api = get_api()


def search(query, count):
    return [status for status in tweepy.Cursor(api.search, q=query).items(count)]
    
tweets = search("#Friday", 1)
first_tweet = tweets[0]

print("Text of tweet: " + first_tweet.text)
print("Screen Name of User: " + first_tweet.user.screen_name)
hashtags = [ h['text'] for h in first_tweet.entities['hashtags']]
print("Hashtags: " + str(hashtags))
print("User Follower Count: " + str(first_tweet.user.followers_count))
print("User Follows Count: " + str(first_tweet.user.friends_count))
print("User Tweet Count: " + str(first_tweet.user.statuses_count))

usr = round(first_tweet.user.followers_count / first_tweet.user.friends_count, 2)
print("User Sucks Ratio: " + str(usr))
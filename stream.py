from tweepy import Stream
from tweepy.streaming import StreamListener
from auth import get_auth

keyword_list = ['mocion de censura']
limit = 50

class MyStreamListener(StreamListener):
    
    def __init__(self):
        super(MyStreamListener, self).__init__()
        self.num_tweets = 0
        
    def on_data(self, data):
        if self.num_tweets < limit:
            self.num_tweets += 1
            try: 
                with open()
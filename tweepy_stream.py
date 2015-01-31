import sys
import tweepy
import twitter
import subprocess



consumer_key="zNKX8aerJVc1SkYLINQHg"
consumer_secret="aywSxm4Un1okiDtZLg2ZjSz0WYt09azXz6i9xoXA"
access_key = "1648701380-HMIJhfzyOF7JBTRqA1uBl65UrI7973i7ZbsHiyv"
access_secret = "CNXoWPryDyjingxQMantJQRybKC6yWh4xnxLv3og"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth)
count  = 0
class CustomStreamListener(tweepy.StreamListener):
    def on_status(self, status):
        global count
        #import pdb; pdb.set_trace()
        print status.text # str(status.id)
        #Getting tweet_id from twitter_stream to reply
        tweet_id = open('tweet_id.txt','w')
        tweet_id.write(str(status.id))
        tweet_id.close()

        screen_name = open('screen_name.txt', 'w')
        screen_name.write(str(status.user.screen_name))
        screen_name.close()

        # tweet_id = status.id
        # username = status.user.screen_name
        # print username

        #tweepy can do update_status
        #pi.update_status("@%s : Hello?"%username, in_reply_to_status_id = tweet_id)
        
        subprocess.call(["python","/Users/ilwonyoon/Dropbox/itp2013_fall/approriating_technology/week1_social_glitch/twython-3.1.0/twitter_reply.py"])
        

       
        return False    # This is commented out so the script will continue to run after finding a tweet

    def on_error(self, status_code):
        print >> sys.stderr, 'Encountered error with status code:', status_code
        return True # Don't kill the stream

    def on_timeout(self):
        print >> sys.stderr, 'Timeout...'
        return True # Don't kill the stream

twitter_stream = tweepy.streaming.Stream(auth, CustomStreamListener())

#Searching for the string
iterator = twitter_stream.filter(track=['I am all alone'])
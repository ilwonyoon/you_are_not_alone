######################################################################
#This file should be placed on the same folder with twython library.##
######################################################################
import random
import sys
from twython import Twython
#Using oauth_1 to access personal account.
#Using oauth_2 to access an application


APP_KEY = 'zNKX8aerJVc1SkYLINQHg'
APP_SECRET='aywSxm4Un1okiDtZLg2ZjSz0WYt09azXz6i9xoXA'
OAUTH_TOKEN= '1648701380-HMIJhfzyOF7JBTRqA1uBl65UrI7973i7ZbsHiyv'
OAUTH_TOKEN_SECRET='CNXoWPryDyjingxQMantJQRybKC6yWh4xnxLv3og'


imagestock ={
	"1":"/Users/ilwonyoon/Dropbox/itp2013_fall/approriating_technology/week1_social_glitch/notalone.jpg",	
	"2":"/Users/ilwonyoon/Dropbox/itp2013_fall/approriating_technology/week1_social_glitch/notalone1.jpg",
	"3":"/Users/ilwonyoon/Dropbox/itp2013_fall/approriating_technology/week1_social_glitch/notalone2.jpg",
	"4":"/Users/ilwonyoon/Dropbox/itp2013_fall/approriating_technology/week1_social_glitch/notalone3.jpg",
	"5":"/Users/ilwonyoon/Dropbox/itp2013_fall/approriating_technology/week1_social_glitch/notalone4.jpg",
	"6":"/Users/ilwonyoon/Dropbox/itp2013_fall/approriating_technology/week1_social_glitch/notalone5.jpg",
	"7":"/Users/ilwonyoon/Dropbox/itp2013_fall/approriating_technology/week1_social_glitch/notalone6.jpg",
	"8":"/Users/ilwonyoon/Dropbox/itp2013_fall/approriating_technology/week1_social_glitch/notalone7.jpg",
	"9":"/Users/ilwonyoon/Dropbox/itp2013_fall/approriating_technology/week1_social_glitch/notalone8.jpg",
	"10":"/Users/ilwonyoon/Dropbox/itp2013_fall/approriating_technology/week1_social_glitch/notalone9.jpg",
	


}
randKey = random.choice(imagestock.keys())

imgURL= imagestock[randKey]
#photo= open('/home/pi/ThankYouDuck/camera/my_gif.GIF')
photo= open(imgURL)


twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN,OAUTH_TOKEN_SECRET)
twitter.verify_credentials()

# who_mention = open('/home/pi/thankyouduck/who.txt')

# user_data = who_mention.readline().split(" ")
# username = user_data[0]
#tweet_id = user_data[len(user_data)-1]
#status='@'+ username +'I am inflated :) '+ ''

#text to go to twitter


#Retrieve tweet id and screen_name
tweet_id =open('/Users/ilwonyoon/Dropbox/itp2013_fall/approriating_technology/week1_social_glitch/tweet_id.txt').readline()
screen_name = open('/Users/ilwonyoon/Dropbox/itp2013_fall/approriating_technology/week1_social_glitch/screen_name.txt').readline()
status= '@%s, You are not alone'%screen_name
print tweet_id

twitter.update_status_with_media(media=photo,
                                 status=status,
                                 in_reply_to_status_id=tweet_id)
print "Tweet back to the user"

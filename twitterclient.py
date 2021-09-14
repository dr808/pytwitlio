import tweepy
import os
import sys


# Init Twitter Vars
try:
    # Sets Keys, Tokens, etc.
    consumer_key = os.environ['TWITTER_CONSUMER_KEY']
    consumer_secret = os.environ['TWITTER_CONSUMER_SECRET']
    access_token = os.environ['TWITTER_ACCESS_TOKEN']
    access_token_secret = os.environ['TWITTER_ACCESS_TOKEN_SECRET']
except KeyError:
    sys.exit('Must supply valid Twitter Tokens. See Readme')

try:
    # Sets TwitterIds
    var_twitterids = list((os.environ['TWITTERIDS']).split(','))
    twitterids = []
    for phrase in var_twitterids:
        twitterids.append(phrase.strip())
except KeyError:
    sys.exit('Must supply valid Twitter Ids. See Readme')

try:
    # Sets Trackwords
    var_trackwords = list((os.environ['TRACKWORDS']).split(','))
    trackwords = []
    for phrase in var_trackwords:
        trackwords.append(phrase.strip())
except KeyError:
    sys.exit('Must supply valid Trackwords. See Readme')

# try:
    # Alow RT?
allow_rt = os.environ.get("ALLOW_RT", False)
if str(allow_rt).lower() in ('true', 'yes', '1', 't'):
    allow_rt = True
else:
    allow_rt = False
# except (KeyError, Exception):
#     allow_rt = False


# Initialize Twitter
try:
    # Sets Tweepy Auth Vars
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    # Auths Tweepy
    api = tweepy.API(auth)
except KeyError:
    sys.exit('Failed to init Tweepy Client')

#import required modules
import tweepy
from tqdn import tqdn
import numpy as np
import json
import pandas as pd
from matplotlib import pyplot as plt
%matplotlib inline

auth=tweepy.OAuthHandler('')
auth.set_access_token('')

api=tweepy.API(auth)

username='VedVyasPB'
tweets=tweepy.Cursor(api.user_timeline,screen_name=username,tweet_mode='extended').items()
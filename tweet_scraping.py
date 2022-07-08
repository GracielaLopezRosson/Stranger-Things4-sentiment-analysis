# -*- coding: utf-8 -*-
"""
Created on Thu Oct 14 16:18:15 2021

@author: graci
"""

"""
Twitter scraping API
"""

import tweepy
import pandas as pd
import time

# Credentials

consumer_key = "Hiv7pGXNN8nCJTDgGq6j3FOSF"
consumer_secret = "hv0sLsiQl03WwfexlQXffMUo0SC2sI1iCJ08HWNbunAiVrCz0l"
access_token = "41203807-aqfFYXH5JiSEZUsTjWGW3NXu6TSKlBdIp2eEAjQtv"
access_token_secret = "C1Y4xEyjqvIJVsnpMz4Mkhol4cUiNuHuh6XQp7dAzcWe1"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth,wait_on_rate_limit=True)


tweets = []

def text_query_to_csv(text_query,count):
    try:
        # Creation of query method using parameters
        #q=text_query -filter:retweets
        tweets = tweepy.Cursor(api.search_tweets, q=text_query + '-filter:retweets', lang="en").items(count)

        # Pulling information from tweets iterable object
        #if (not tweets.retweeted) and ('RT @' not in tweets.text):
        tweets_list = [[tweet.created_at, tweet.id, tweet.text] for tweet in tweets]

        # Creation of dataframe from tweets list
        # Add or remove columns as you remove tweet information
        
        tweets_df = pd.DataFrame(tweets_list, columns=['Datetime', 'Tweet Id', 'Text'])
        
        
        # Converting dataframe to CSV 
        tweets_df.to_csv('{}-tweets.csv'.format(text_query), sep=',', index = False)

    except BaseException as e:
        print('failed on_status,',str(e))
        time.sleep(3)
        

# Input search query to scrape tweets and name csv file
# Max recent tweets pulls x amount of most recent tweets from that user
text_query = '#strangerthingsseason4'
count = 5000

# Calling function to query X amount of relevant tweets and create a CSV file
text_query_to_csv(text_query, count)
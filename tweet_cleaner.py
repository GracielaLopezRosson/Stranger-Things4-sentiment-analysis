# -*- coding: utf-8 -*-
"""
Created on Thu Oct 14 18:32:56 2021

@author: graci
"""

"""
CLEAN TWEETS FROM SPECIAL CHARACTERS? SYMBOLS AND EMOJIS
"""
from textblob import TextBlob
from emoji_translate.emoji_translate import Translator
import nltk
import pandas as pd
import re


def cleaner(tweet):
    tweet = re.sub("@[A-Za-z0-9]+","",tweet) #Remove @ sign
    tweet = re.sub(r"(?:\@|http?\://|https?\://|www)\S+", "", tweet) #Remove http links
    tweet = " ".join(tweet.split())
    tweet = tweet.replace("#", "").replace("_", " ") #Remove hashtag sign but keep the text
    tweet = tweet.replace("_", " ") # sign but keep the text

    tweet = " ".join(w for w in nltk.wordpunct_tokenize(tweet)
         if w.lower() in words or not w.isalpha())
    return tweet

nltk.download('words')
words = set(nltk.corpus.words.words())

def translate_emojis(tweet):
    emo = Translator(exact_match_only=False, randomize=True)
    tweet_translated = emo.demojify(tweet)
    return tweet_translated
    


df = pd.read_csv('#strangerthingsseason4-tweets_nofiltered.csv')

df_clean = df.copy()
df_clean['tweet_clean'] = df_clean['Text'].apply(cleaner)
df_clean['no_emoji'] = df_clean['tweet_clean'].apply(translate_emojis)

df_clean.to_csv('df.csv')








# #Function to Create Wordcloud
# def create_wordcloud(text):
#  mask = np.array(Image.open(“cloud.png”))
#  stopwords = set(STOPWORDS)
#  wc = WordCloud(background_color=”white”, mask = mask, max_words=3000,
#  stopwords=stopwords, repeat=True)
#  wc.generate(str(text))
#  wc.to_file(“wc.png”)
#  print(“Word Cloud Saved Successfully”)
#  path=”wc.png”
__author__ = 'Ciaran Griffin t00175569'

import pymongo
from pymongo import MongoClient


client = MongoClient()

db = client.cooldb

print db

collection = db.cooltweets

print collection.count()

tweets_iterator = collection.find()
for tweet in tweets_iterator:
    tweet_text = tweet['text']
    if
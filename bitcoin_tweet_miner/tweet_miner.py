__author__ = 'Ciaran Griffin t00175569'

import tweepy
from pymongo import MongoClient

consumer_key = "xwYcAPXSdevBROW45G4l5JwlW"
consumer_secret = "EChw4DZkXZ84hkjJog93zDxU2NazyXd2LldqT84bwkHvuirhGG"
access_token = "240685217-vxGVT3E4I7WOVd2ihglVYpXwiXvI0xXtmu6uQPTG"
access_token_secret = "X4ivkvI4K9LUVCs3y7BF8OXCudwezU3hnToKPyqybPEjl"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

results = api.search(q="trump")

client = MongoClient()
db = client.test_db
collection = db.test_collection
post = {"name": "Ciaran", "awesome_at": ["Java", "Python", "MongoDb", "Tweepy"]}
posts = db.posts
post_id = posts.insert_one(post).inserted_id
# print post_id.type()
# print posts.find_one ()
# ans = posts.find_one({"name": "Ciaran"})
# print ans
new_posts = [{"author": "Mike",
              "text": "Another post!",
              "tags": ["bulk", "insert"],
              },
             {"author": "Eliot",
              "title": "MongoDB is fun",
              "text": "and pretty easy too!",
              }]
result = posts.insert_many(new_posts)
print result.inserted_ids
x = 2556.95
gd = x * 0.7 * 1.23
print gd
print x -  gd
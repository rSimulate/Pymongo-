__author__ = 'martin'
import pymongo
import datetime
import ssl

from pymongo import MongoClient


client = MongoClient('54.187.94.3',27017)


#client = MongoClient('54.187.94.3',27017,
#        ssl=True,
#    ssl_certfile='/home/martin/spaceapp.pem'
#    )




db=client.test_database2
collection=db.test_collection2

post={"author":"Martin",
      "text":"Hello World",
      "tags":["mongod","python","pymongo"],
      "date":datetime.datetime.utcnow()}

posts=db.posts
post_id = posts.insert(post)

post_id
db.collection_names()

print posts.find_one({"author":"Mark"})
__author__ = 'martin'
import pymongo
import datetime
import ssl
from pymongo import MongoClient


#client = MongoClient('54.187.94.3',27017)

client = MongoClient('data.asteroid.ventures',27017)
#client = MongoClient('54.187.94.3',27017,
#        ssl=True,
#    ssl_certfile='/home/martin/spaceapp.pem'
#    )




db=client.toms_weiner
collection=db.toms_weiner

post={"author":"Martin",
      "text":"Goodbye World",
      "tags":["mongod","python","pymongo"],
      "date":datetime.datetime.utcnow()}


posts=db.posts
posts.insert(post)


db.collection_names()

print posts.find_one({"author":"Martin"},{"text":1,"_id":0})

posts.update({'_id':p['_id']},{'$inc':{'d.a': 1}},upsert=False, multi=False)

for p in productData.find():
     for k,v in p.iteritems():
         value=v['a']
         value=value+1
         v['a']=value
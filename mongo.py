import pymongo
import os
import env

MONGODB_URI = os.getenv("MONGO_URI", 'No ENV Value')
DBS_NAME = "test"
COLLECTION_NAME = "myTestDB"


def mongo_connect(url):
    try:
        conn = pymongo.MongoClient(url)
        print("Mongo Is Connected")
        return conn
    except pymongo.errors.ConnectionFailure as e:
        print("Could not connect to MongoDB: %s") % e


conn = mongo_connect(MONGODB_URI)

coll = conn[DBS_NAME][COLLECTION_NAME]

coll.update_one({'last': 'singh'}, {'$set': {'last': 'tariq'}})
documents = coll.find()

for doc in documents:
    print(doc)

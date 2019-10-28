import pymongo
import os

MONGODB_URI = os.getenv("MONGO_URI")
DBS_NAME = "test"
COLLECTION_NAME = "myFirstMDB"


def mongo_connect(url):
    try:
        conn = pymongo.MongoClient(url)
        return conn
    except pymongo.errors.ConnectionFailure as e:
        print("Could Not Connect To MongoDB: %s") % e

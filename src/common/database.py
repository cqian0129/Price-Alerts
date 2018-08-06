import os
import pymongo


class Database(object):
    URI = "mongodb://cheng_test:cheng123@ds155718.mlab.com:55718/heroku_kltm4wr6"
    DATABASE = None

    @staticmethod
    def initialize():
        client = pymongo.MongoClient(Database.URI)
        Database.DATABASE = client['heroku_kltm4wr6']

    @staticmethod
    def insert(collection, data):
        Database.DATABASE[collection].insert(data)

    @staticmethod
    def find(collection, query):
        return Database.DATABASE[collection].find(query)

    @staticmethod
    def find_one(collection, query):
        return Database.DATABASE[collection].find_one(query)

    @staticmethod
    def update(collection, query, data):
        Database.DATABASE[collection].update(query, data, upsert=True)

    @staticmethod
    def remove(collection, query):
        return Database.DATABASE[collection].remove(query)
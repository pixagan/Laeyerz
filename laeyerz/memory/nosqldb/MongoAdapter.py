# Created: Anil Variyar
# MongoDB Adapter

import os
from pymongo import MongoClient

filepath = os.getenv('MONGO_URI')
mongo_db = os.getenv('MONGO_DB')



class MongoAdapter:

    def __init__(self):
        self.client = MongoClient(os.getenv('MONGO_URI'))
        self.db     = self.client[os.getenv('MONGO_DB')]
        #self.collection = self.db[os.getenv('MONGO_COLLECTION')]


    def create(self, collection_name, data):
        """Create a new document in MongoDB"""
       
        newItem = self.db[collection_name].insert_one(data)

        return newItem



    def create_many(self, collection_name, data_list):
        
        print("Creating many",collection_name, data_list)
        
        self.db[collection_name].insert_many(data_list)
        
        



    def read(self, collection_name, query):
        """Read documents matching the query"""
        return self.db[collection_name].find(query)





    def read_one(self, collection_name, query):
        """Read a single document matching the query"""
        return self.db[collection_name].find_one(query)



    def update(self, collection_name, query, new_values):
        """Update documents matching the query"""
        return self.collection.update_many(query, {'$set': new_values})



    def delete(self, collection_name, query):
        """Delete documents matching the query"""
        return self.collection.delete_many(query)



    def close(self):
        """Close the MongoDB connection"""
        self.client.close()
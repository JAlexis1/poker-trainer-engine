import os
from pymongo import MongoClient

class BaseRepository:
    def __init__(self, client: MongoClient = None):
        if client is None:
            mongo_uri = os.getenv("MONGO_URI", "mongodb://localhost:27017/")
            self.client = MongoClient(mongo_uri)
        else:
            self.client = client
            
        db_name = os.getenv("MONGO_DB_NAME", "poker_training_db")
        self.db = self.client[db_name]
# db.py
from pymongo import MongoClient
from config.config import MONGO_URI, DATABASE_NAME

cliente = MongoClient(MONGO_URI)
db = cliente[DATABASE_NAME]

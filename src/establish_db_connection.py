from pymongo import MongoClient 


client = MongoClient("mongodb://localhost:27017")
# client = MongoClient("localhost:27017")
database = client.HeartDiseasePrediction

# importing the needed libraries
import pandas as pd
from pymongo import MongoClient


# Connecting to the MongoDB Database, and creating a database
client = MongoClient("mongodb://mongo:27017/")  # "mongo" ist der Name des MongoDB-Services im docker-compose.yml
db = client["portfolio_database"]
collection = db["co2_data"]


#Reading CSV File and storing it in batchesto the collection 
chunk_size = 50
for chunk in pd.read_csv("iot_telemetry_data.csv", chunksize=chunk_size):
    # Daten in MongoDB einfügen
    records = chunk.to_dict(orient="records")
    collection.insert_many(records)


print("Import completed.")

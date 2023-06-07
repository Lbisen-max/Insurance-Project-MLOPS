import pymongo 
from pymongo.mongo_client import MongoClient
import pandas as pd
import json



uri = "mongodb+srv://Lokesh11:Delta21@cluster0.ceqxwjb.mongodb.net/?retryWrites=true&w=majority"

# Create a new client and connect to the server
client = MongoClient(uri)

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

DATA_FILE_PATH = "D:\ML Projects\Insurance\Insurance-ML-Project\insurance.csv"
DATABASE_NAME = "INSURANCE"
COLLECTION_NAME = "INSURANCE_PROJECT"

if __name__=="__main__":
    df = pd.read_csv(DATA_FILE_PATH)
    # checking the shape ogf data
    print(f"Row and columns: {df.shape}")

    # our data has index also which we can drop
    df.reset_index(drop=True,inplace=True)

    # since mongodb takes data into key and value hecne we have to transpose the data and have to convert into json

    json_record = list(json.loads(df.T.to_json()).values())
    print(json_record[0])

    # Inserting the data into mongodb
    client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_record)
from pymongo.mongo_client import MongoClient
import pandas as pd
import json

url="mongodb+srv://mohit:1234@cluster0.fv0zy.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
#create a new client
client=MongoClient(url)
#create a database name and collection name
DATABASE_NAME='sensor_fault'
COLLECTION_NAME='sensor_fault_'
df=pd.read_csv("C:\Users\91879\OneDrive\Desktop\Sensor_Project\notebooks\wafer_23012020_041211.csv")
df=df.drop("Unnamed: 0",axis=1)
json_record=list(json.loads(df.T.to_json()).values())
json_record
client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_record)
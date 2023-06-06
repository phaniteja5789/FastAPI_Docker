from fastapi import FastAPI
import requests
import json
from pymongo import MongoClient
from datetime import date

app=FastAPI()
url="https://randomuser.me/api/"
client=MongoClient('mongodb://mongodb:27017/')
db=client.get_database("Dockeruser")
collection=db.get_collection("user")
if collection is None:
    collection=db.create_collection("user")

def CreateUser():
    data=requests.get(url,auth=('user','pass')).text
    json_data=json.loads(data)
    result=json_data["results"][0]
    name=json.dumps(result["name"])
    location=json.dumps(result["location"])
    age=str(result["dob"]["age"])
    email=str(result["email"])
    gender=str(result["gender"])
    user={}
    user["name"]=name
    user["age"]=age
    user["location"]=location
    user["gender"]=gender
    user["email"]=email
    collection.insert_one(user)

@app.get("/")
def AddUser():
    CreateUser()
    return "Insertion Completed"


if __name__=="__main__":
    app()
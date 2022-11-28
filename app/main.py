import os
from fastapi import FastAPI, Body, HTTPException, status
from fastapi.responses import Response, JSONResponse
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel, Field, EmailStr
from bson import ObjectId
from typing import Optional, List
import motor.motor_asyncio

# Relative/Local Imports 
from models import PyObjectId, UserIDModel, UserModel

app = FastAPI()
client = motor.motor_asyncio.AsyncIOMotorClient(os.environ["MONGODB_URL"])
db = client.Generic_Bunkies


# ***** BEGIN ENDPOINTS *****

# @app.get("/", response_description="Default Landing Page")
@app.get("/", response_description="Default Landing Page")
async def index():
    return {"title": "Welcome to Bunkiez!"}
    # return students

@app.get("/user", response_model=UserModel)
async def user(id: PyObjectId):
    if (user := await db["UserbaseB"].find_one({"_id": id})) is not None:
        return user
    
    raise HTTPException(status_code=404, detail=f"User ID {id} not found")
    

# parameter: number of User IDs
@app.get("/users", response_description="List all User IDs", response_model=List[UserIDModel])
async def users(count: int = 1000):
    count = min(count, 1000)
    return await db["UserbaseB"].find().to_list(count)

@app.get("/usersB")
async def usersB():
    # poll database
    # return ALL users?
    
    # from pymongo import MongoClient
    # db_auth_uri = "mongodb+srv://GenericUser:Bunkiez@bunkiesv1.jzrjtev.mongodb.net/BunkiesV1"
    # client = MongoClient(db_auth_uri)
    # db = client['Generic_Bunkies']
    # # db.list_collection_names()
    # coll_usersB = db['UserbaseB']
    # return coll_usersB.find_one()

    return {"User":"Information"}


@app.get("/matches")
def matches():
    # fetch all users
    # perform matching algorithm
    # return id's of relevant matches
    return {"User":"Information"}

"""
@app.post("/register")
def register():
    return {"User":"Information"}

@app.post("/auth")
def auth():
    # return a JWT token
    return {"Token":"encoded_token"}

@app.post("/login")
def auth():
    # return a JWT token
    return {"Token":"encoded_token"}
"""


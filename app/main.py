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

from auth import * # Token, TokenData, User, UserInDB


# # JWT Auth dependencies
# from datetime import datetime, timedelta
# from fastapi import Depends
# from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
# from jose import JWTError, jwt
# from passlib.context import CryptContext

# # JWT AUTH Config 
# pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
# oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


app = FastAPI()
client = motor.motor_asyncio.AsyncIOMotorClient(os.environ["MONGODB_URL"])
db = client.Generic_Bunkies


# ***** BEGIN ENDPOINTS *****

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





@app.post("/token", response_model=Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(fake_users_db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}


@app.get("/users/me/", response_model=User)
async def read_users_me(current_user: User = Depends(get_current_active_user)):
    return current_user


@app.get("/users/me/items/")
async def read_own_items(current_user: User = Depends(get_current_active_user)):
    return [{"item_id": "Foo", "owner": current_user.username}]
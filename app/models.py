from pydantic import BaseModel, Field, EmailStr
from bson import ObjectId


# https://www.mongodb.com/developer/languages/python/python-quickstart-fastapi/
class PyObjectId(ObjectId):
    """ Custom Type for reading MongoDB IDs """
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not ObjectId.is_valid(v):
            raise ValueError("Invalid objectid")
        return ObjectId(v)

    @classmethod
    def __modify_schema__(cls, field_schema):
        field_schema.update(type="string")


class UserIDModel(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    class Config:
        allow_population_by_field_name = True
        # arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}



class UserModel(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    # email: EmailStr = Field(...)
    contactEmail: str = Field(...)
    name: str = Field(...)
    gender: str = Field(...)
    
    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {
            "example": {
                "email": "jdoe@example.com",
                "passwordHash": "jdoe@example.com",
                "name": "Jane Doe",
                "gender": "Female",
            }
        }

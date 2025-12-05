from pydantic import BaseModel, validator
from datetime import datetime
# Példa: API request/response schema
class ReqUserFull(BaseModel):
    id: int | None = None
    user_role: str | None = None
    firstname: str | None = None
    lastname: str | None = None
    file_path: str | None = None
    time_last_login: datetime | None = None

    # Validator, ha stringből jön
    @validator("time_last_login", pre=True)
    def parse_last_login(cls, v):
        if isinstance(v, str):
            return datetime.strptime(v, "%Y-%m-%d %H:%M:%S.%f")
        return v

    # JSON formátum testreszabása
    class Config:
        json_encoders = {
            datetime: lambda v: v.strftime("%Y-%m-%d %H:%M:%S.%f")
        }

class ReqUser(BaseModel):
    id: int
    user_role:str
    firstname:str
    lastname:str
    time_last_login:datetime
    # Validator, ha stringből jön
    @validator("time_last_login", pre=True)
    def parse_last_login(cls, v):
        if isinstance(v, str):
            return datetime.strptime(v, "%Y-%m-%d %H:%M:%S.%f")
        return v

    # JSON formátum testreszabása
    class Config:
        json_encoders = {
            datetime: lambda v: v.strftime("%Y-%m-%d %H:%M:%S.%f")
        }

class ReqUserBase(BaseModel):
    firstname:str
    lastname:str
    file_url:str
    time_last_login:datetime
    # Validator, ha stringből jön
    @validator("time_last_login", pre=True)
    def parse_last_login(cls, v):
        if isinstance(v, str):
            return datetime.strptime(v, "%Y-%m-%d %H:%M:%S.%f")
        return v

    # JSON formátum testreszabása
    class Config:
        json_encoders = {
            datetime: lambda v: v.strftime("%Y-%m-%d %H:%M:%S.%f")
        }

class UserCreate(BaseModel):
    firstname:str
    lastname:str
    email:str
    phone_number:str
    password:str
    country:str
    zip:str
    city:str
    street:str
    house_number:str

class UserLoginEmail(BaseModel):
    email:str
    password:str

class UserUpdate(BaseModel):
    user_role:str|None = None
    email:str|None = None
    country:str|None = None
    zip:str|None = None
    city:str|None = None
    street:str|None = None
    house_number:str|None = None

class UserId(BaseModel):
    id:int

from pydantic import BaseModel

# Példa: API request/response schema
class User(BaseModel):
    id: int
    username:str
    password:str
    

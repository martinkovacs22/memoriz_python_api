# routers/user.py
import os
from fastapi import APIRouter ,HTTPException, Response
from schemas.User import UserCreate , UserLoginEmail ,ReqUserFull
from services.User import sp_UserCreate ,sp_UserLoginEmail
from services.jwt_service import ACCESS_TOKEN_EXPIRE_MINUTES ,create_access_token
from dotenv import load_dotenv

load_dotenv()

router = APIRouter(
    prefix="/user",
    tags=["User"]
)
#create
@router.post("/")
def user_create(data: UserCreate):
    return {"data":sp_UserCreate(data)}
#login
@router.post("/login")
def user_login(data: UserLoginEmail, response: Response):
    try:
        user: ReqUserFull = sp_UserLoginEmail(data)
    except ValueError as e:
        raise HTTPException(status_code=401, detail=str(e))
    
    COOKIE_JWT_NAME = os.getenv("COOKIE_JWT_NAME")

    # JWT generálása
    token_data = {"user_id": user.id}
    access_token = create_access_token(token_data)
    
    # Cookie-be állítás
    response.set_cookie(
        key=COOKIE_JWT_NAME,
        value=access_token,
        httponly=True,      # JS nem tudja olvasni
        max_age=ACCESS_TOKEN_EXPIRE_MINUTES * 60,
        samesite="lax"      # CSRF elleni védelemhez
    )

    # Visszaküldhetjük a user adatait is
    return {"user": user}
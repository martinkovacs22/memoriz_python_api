# routers/user.py
from fastapi import APIRouter
from schemas.User import User
router = APIRouter(
    prefix="/user",
    tags=["User"]
)

@router.get("/{id}")
def get_user_by_id(id: int):
    return {"id": id}

@router.post("")
def get_all_user(data: User):
    return {"data":data}


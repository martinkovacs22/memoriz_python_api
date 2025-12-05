from schemas.User import UserCreate ,UserLoginEmail ,ReqUserFull

from services.Store_Proseder import call_stored_procedure 

def sp_UserCreate(user:UserCreate):
    return call_stored_procedure("userCreate",user)

# 2. Stored procedure meghívása és átalakítás
def sp_UserLoginEmail(user: UserLoginEmail) -> ReqUserFull:
    # Meghívjuk a stored procedure-t
    result = call_stored_procedure("userLoginEmail", user)
    
    # A call_stored_procedure list of list-et ad vissza, pl. [[{...}]]
    # Vegyük az első SELECT-et és az első sort
    if result and result[0]:
        user_data = result[0][0]  # első row
        # Átalakítás ReqUserFull BaseModel-é
        return ReqUserFull(**user_data)
    else:
        raise ValueError("User not found or invalid credentials")

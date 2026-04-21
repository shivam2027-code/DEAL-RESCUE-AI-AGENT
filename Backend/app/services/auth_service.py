from fastapi import HTTPException


from app.repositories.user_repo import get_user_by_email , create_user

from app.core.security import hash_password , verify_password
from app.core.jwt import create_access_token

def signup_user(data,db):
    existing_user = get_user_by_email(db,data.email)

    if existing_user:
        raise HTTPException(status_code=400 , detail="user already exists")
    
    hashed = hash_password(data.password)

    user = create_user(db,data.email,hashed,data.name)

    token = create_access_token({"sub":user.email})

    return{
        "message":"user created",
        "access_token":token,
    }

def login_user(data,db):
    user = get_user_by_email(db , data.email)

    if not user:
        raise HTTPException(status_code=404,detail="user not found")
    
    if not verify_password(data.password,user.password):
        raise HTTPException(status_code=401,detail="paasword incorrect")
    
    token = create_access_token({"sub":user.email})

    return {
        "msg":"login succesfully",
        "access_token":token
    }

from fastapi import APIRouter  , HTTPException , Depends

from sqlalchemy.orm import Session
from app.schemas.auth import LoginRequest , SignupRequest
from app.db.database import sessionLocal , get_db
from app.models.user_model import User
from app.services.auth_service import signup_user  , login_user

auth_router = APIRouter(prefix="/auth")


@auth_router.post("/signup")
def signUp(data:SignupRequest , db:Session=Depends(get_db)):
    return signup_user(data,db)


@auth_router.post("/login")
def login(data:LoginRequest,db:Session=Depends(get_db)):
    return login_user(data,db)

    


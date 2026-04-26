from app.models.user_model import User

def get_user_by_email(db,email:str):
    return db.query(User).filter(User.email == email).first()


def create_user(db , email:str,hashed_password:str,name:str):
    user = User(email=email ,password=hashed_password,name=name)

    db.add(user)
    db.commit()
    db.refresh(user)

    return user
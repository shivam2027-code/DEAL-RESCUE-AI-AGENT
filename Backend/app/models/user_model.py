from sqlalchemy import Column , Integer , String , DateTime , Boolean
from app.db.database import Base
from datetime import datetime

class User(Base):
    __tablename__ = "users"

    id = Column(Integer ,primary_key=True , index=True )
    email = Column(String , unique=True ,nullable=False)
    password = Column(String ,nullable=False )
    name = Column(String , default="User")
    is_active = Column(Boolean , default=True , nullable=False)
    created_at = Column(DateTime , default=datetime.utcnow)
    updated_at = Column(DateTime , default=datetime.utcnow , onupdate=datetime.utcnow)
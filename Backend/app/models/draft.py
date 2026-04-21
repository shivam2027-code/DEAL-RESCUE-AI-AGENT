from sqlalchemy import Column , String  , Integer , DateTime
from app.db.database import Base

class Draft(Base):
    __tablename__ = "Drafts"
    id = Column(Integer , primary_key=True,index=True)
    reply = Column(String)
    status = Column(String , default="pending")
    event_id = Column(Integer)
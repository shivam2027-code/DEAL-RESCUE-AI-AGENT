from sqlalchemy import Column , String  , DateTime , Integer
from datetime import datetime
from app.db.database import Base

class Event(Base):
    __tablename__ = "events"
    id = Column(Integer , primary_key=True , index=True)
    email = Column(String)
    sender = Column(String, nullable=False)
    event_type = Column(String)
    timestamp = Column(DateTime , default=datetime.utcnow)  
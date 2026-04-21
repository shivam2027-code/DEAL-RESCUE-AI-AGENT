from sqlalchemy import Column , String  , Integer , DateTime
from app.db.database import Base


class Risk(Base):
    __tablename__ = "risks"
    id = Column(Integer , primary_key=True , index=True)
    competitor = Column(String , default=None)
    risk_type = Column(String)
    event_id = Column(Integer)
    
from sqlalchemy.ext.declarative  import declarative_base
from sqlalchemy.orm import sessionmaker , Session
from sqlalchemy import create_engine
from app.core.config import getAppConfig
from typing import Generator


config = getAppConfig()

Base = declarative_base()

engine = create_engine(config.database_url)

sessionLocal = sessionmaker(autoflush=False , autocommit=False , bind=engine)

def get_db()-> Generator[Session , None , None]:
    db = sessionLocal()
    try:
        yield db

    finally:
        db.close()    

        
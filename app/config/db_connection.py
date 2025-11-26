from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

import os

from dotenv import load_dotenv

load_dotenv()

DB_STRING = os.getenv("CONNETION_STRING")

engine = create_engine(DB_STRING)

Base = declarative_base()

SessionLocal = sessionmaker(autocommit=False,autoflush=False,bind=engine)

def get_session():

    db=SessionLocal()
    
    try:
        yield db
    finally:
        db.close()
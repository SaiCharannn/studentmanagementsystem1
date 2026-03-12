from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = "postgresql://postgres:Schar%402003@localhost/student_db"

engine = create_engine(DATABASE_URL)

SessionLocal =  sessionmaker(bind=engine)

BASE = declarative_base() 
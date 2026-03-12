from sqlalchemy import Column,Integer,String,Boolean, text
from app.database import BASE

class Place(BASE):
  __tablename__ = "master_place"

  id = Column(Integer, primary_key=True)
  name =Column(String(100), unique = True ) 
  is_active = Column(Boolean, nullable=False, server_default=text("true"))
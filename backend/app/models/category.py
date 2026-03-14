from sqlalchemy import Column,Integer,String,Boolean, text
from app.database import BASE

class Category(BASE):
  __tablename__ = "master_studentcategory"
  id = Column(Integer,primary_key=True)
  name =Column(String(50)) 
  is_active = Column(Boolean, nullable=False, server_default=text("true"))


from sqlalchemy import Column,Integer,String,Boolean,text
from app.database import BASE

class Course(BASE):
  __tablename__ = "master_course"
  id = Column(Integer, primary_key=True)
  name = Column(String(100))
  duration_months = Column(Integer)    
  is_active = Column(Boolean, nullable=False, server_default=text("true"))

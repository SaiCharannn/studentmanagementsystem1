from sqlalchemy import Column, Integer, String, Date, ForeignKey
from app.database import BASE
from sqlalchemy.orm import relationship

class Student(BASE):
  __tablename__ = "student_master"
  id = Column(Integer, primary_key= True, index=True)
  student_id = Column(String, unique=True)
  name = Column(String(100))
  fathers_name = Column(String(100))
  date_of_birth = Column(Date)

  place_id = Column(Integer,ForeignKey("master_place.id"))
  course_id =Column(Integer,ForeignKey("master_course.id"))
  category_id =Column(Integer,ForeignKey("master_studentcategory.id")) 
  
  place = relationship("Place")
  course = relationship("Course")
  category = relationship("Category")
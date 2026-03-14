from sqlalchemy.orm import Session
from app.models.place import Place
from app.models.course import Course
from app.models.category import Category

def get_places(db: Session):
    return db.query(Place).all()

def get_courses(db: Session):
    return db.query(Course).all()

def get_categories(db: Session):
    return db.query(Category).all()
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import SessionLocal
from app.crud import master_crud

router = APIRouter()

def get_db():
  db = SessionLocal()
  try:
    yield db
  finally:
    db.close()

@router.get("/api/masters/places/")
def get_places(db: Session = Depends(get_db)):
  return master_crud.get_places(db)

@router.get("/api/master/courses/")
def get_courses(db: Session = Depends(get_db)):
  return master_crud.get_courses(db)

@router.get("/api/master/categories")
def get_categories(db: Session = Depends(get_db)):
  return master_crud.get_categories(db)

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import SessionLocal
from app.schemas.student_schema import StudentCreate
from app.crud import student_crud

router = APIRouter()
def get_db():
    db = SessionLocal()
    try:
      yield db
    finally:
       db.close()

@router.post("/api/students/")
def create_student(student: StudentCreate, db: Session = Depends(get_db)):
   return student_crud.create_student(db,student)

@router.get("/api/students/")
def get_students(db: Session = Depends(get_db)):
   return student_crud.get_students(db)

@router.get("/api/students/{id}")
def get_student(id: int,db: Session = Depends(get_db)):
   return student_crud.get_student(db,id)

@router.put("/api/students/{id}")
def update_student(id: int, student: StudentCreate, db: Session = Depends(get_db)):
    return student_crud.update_student(db, id, student)

@router.delete("/api/students/{id}")
def delete_student(id: int,db:Session = Depends(get_db)):
   student_crud.delete_student(db,id)
   return {"messege":"deleted"}
   

    
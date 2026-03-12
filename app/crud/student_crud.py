from fastapi import HTTPException
from app.models.student import Student
from app.models.place import Place
from app.models.course import Course
from app.models.category import Category


def create_student(db, student):

    existing = db.query(Student).filter(
        Student.student_id == student.student_id
    ).first()

    if existing:
        raise HTTPException(400, "Student ID already exists")

    place = db.query(Place).filter(Place.id == student.place).first()
    course = db.query(Course).filter(Course.id == student.course).first()
    category = db.query(Category).filter(Category.id == student.category).first()

    if not place or not course or not category:
        raise HTTPException(400, "Invalid master reference")

    db_student = Student(
        student_id=student.student_id,
        name=student.name,
        fathers_name=student.fathers_name,
        date_of_birth=student.date_of_birth,
        place_id=student.place,
        course_id=student.course,
        category_id=student.category
    )

    db.add(db_student)
    db.commit()
    db.refresh(db_student)

    return db_student


def get_students(db):
    return db.query(Student).all()


def get_student(db, student_id):
    student = db.query(Student).filter(Student.id == student_id).first()

    if not student:
        raise HTTPException(404, "Student not found")

    return student


def update_student(db, student_id, student):

    db_student = db.query(Student).filter(Student.id == student_id).first()

    if not db_student:
        raise HTTPException(404, "Student not found")

    db_student.student_id = student.student_id
    db_student.name = student.name
    db_student.fathers_name = student.fathers_name
    db_student.date_of_birth = student.date_of_birth
    db_student.place_id = student.place
    db_student.course_id = student.course
    db_student.category_id = student.category

    db.commit()
    db.refresh(db_student)

    return db_student


def delete_student(db, student_id):

    student = db.query(Student).filter(Student.id == student_id).first()

    if not student:
        raise HTTPException(404, "Student not found")

    db.delete(student)
    db.commit()

    return {"message": "Student deleted"}
from pydantic import BaseModel
from datetime import date

class StudentCreate(BaseModel):
    student_id: str
    name: str
    fathers_name: str
    date_of_birth: date
    place: int
    course: int
    category: int


class PlaceResponse(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True


class CourseResponse(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True


class CategoryResponse(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True


class StudentResponse(BaseModel):
    id: int
    student_id: str
    name: str
    fathers_name: str
    date_of_birth: date
    place: PlaceResponse
    course: CourseResponse
    category: CategoryResponse

    class Config:
        orm_mode = True
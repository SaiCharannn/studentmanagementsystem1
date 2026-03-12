from fastapi import FastAPI
from app.database import engine, BASE
from app.models import student, place, course, category
from app.routers import student_router, master_router

app = FastAPI()

# create tables automatically
BASE.metadata.create_all(bind=engine)

app.include_router(student_router.router)
app.include_router(master_router.router)

@app.get("/")
def root():
    return {"message": "Student API running"}
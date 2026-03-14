from fastapi import FastAPI
from app.database import engine, BASE
from fastapi.middleware.cors import CORSMiddleware
from app.routers import student_router, master_router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

BASE.metadata.create_all(bind=engine) # create tables automatically

app.include_router(student_router.router)
app.include_router(master_router.router)

@app.get("/")
def root():
    return {"message": "Student API running"}
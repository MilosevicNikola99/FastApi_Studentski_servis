
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from repositories.student_repository import StudentRepositoriy
from services.student_service import StudentService
app = FastAPI()

class Student(BaseModel):
    id: int
    name: str
    prezime: str
    indeks: str

student_service = StudentService("resources/students.json")
@app.post("/students/")
async def create_student(student: Student):
    student_service.create(student.dict())
    return student.dict()

@app.get("/students/{id}")
async def get_student(id: int):
    return student_service.get_by_id(id)

@app.put("/students/{id}")
async def update_student(id: int, student: Student):
    return student_service.update(id,student.dict())

@app.delete("/students/{id}")
async def delete_student(id: int):
    return student_service.delete(id)

from fastapi import FastAPI,APIRouter
from ..services.student_service import StudentService
from ..schemas.schemas import Student

router = APIRouter()

student_service = StudentService("resources/students.json")
@router.post("/students/",tags=["students"])
async def create_student(student: Student):
    student_service.create(student.model_dump())
    return student.model_dump()

@router.get("/students/{id}",tags=["students"])
async def get_student(id: int):
    return student_service.get_by_id(id)

@router.put("/students/{id}",tags=["students"])
async def update_student(id: int, student: Student):
    return student_service.update(id,student.model_dump())

@router.delete("/students/{id}",tags=["students"])
async def delete_student(id: int):
    return student_service.delete(id)


def get_student_service():
    return student_service
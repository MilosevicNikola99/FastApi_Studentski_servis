from fastapi import FastAPI
from pydantic import BaseModel
from services.exam_service import ExamService
app = FastAPI()

class Exam(BaseModel):
    naziv: str
    sifra_predmeta: str
    espb: int

exam_service = ExamService("resources/exams.json")

@app.post("/exams")
async def create_exam(exam: Exam):
    exam_service.create(exam.model_dump())
    return exam.model_dump()

@app.get("/exams/{exam_code}")
async def get_exam(exam_code: str):
    return exam_service.get_by_code(exam_code)

@app.put("/exams/{exam_code}")
async def update_exam(exam_code: str,exam: Exam):
    return exam_service.update(exam_code,exam.model_dump())

@app.delete("/exams/{exam_code}")
async def delete_exam(exam_code: str):
    return exam_service.delete(exam_code)


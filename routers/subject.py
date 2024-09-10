from fastapi import FastAPI
from pydantic import BaseModel
from services.subject_service import SubjectService
app = FastAPI()

class Subject(BaseModel):
    naziv: str
    sifra_predmeta: str
    espb: int

subject_service = SubjectService("resources/subject.json")

@app.post("/subjects")
async def create_subject(subject: Subject):
    subject_service.create(subject.model_dump())
    return subject.model_dump()

@app.get("/subjects/{subject_code}")
async def get_subject(subject_code: str):
    return subject_service.get_by_code(subject_code)

@app.put("/subjects/{subject_code}")
async def update_subject(subject_code: str,subject: Subject):
    return subject_service.update(subject_code,subject.model_dump())

@app.delete("/subjects/{subject_code}")
async def delete_subject(subject_code: str):
    return subject_service.delete(subject_code)


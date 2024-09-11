from fastapi import FastAPI
from services.exam_services import ExamService
from schemas.schemas import Exam
from schemas.schemas import ExamInfo

app = FastAPI()


exam_service = ExamService("resources/exams.json")

@app.get("/exams/{sifra_predmeta}")
async def get_exams(sifra_predmeta:str):
    return exam_service.get_by_sifra_predmeta(sifra_predmeta)

@app.get("/exams/{indeks}")
async def get_exams(indeks:str):
    return exam_service.get_by_indeks(indeks)

@app.post("/exams/{sifra_predmeta}/{indeks}")
async def create_subject(sifra_predmeta:str,indeks:str ,exam_info : ExamInfo):
    exam_info = exam_info.model_dump()
    exam = Exam(datum= exam_info["datum"],ocena=exam_info["ocena"],polozen=exam_info["polozen"],indeks=indeks,sifra_predmeta=sifra_predmeta)
    exam_service.create(exam.model_dump())
    return exam.model_dump()

@app.put("/exams/{sifra_predmeta}/{indeks}/{datum}")
async def update_subject(sifra_predmeta:str,indeks:str,datum:str,exam_info : ExamInfo):
    return exam_service.update(sifra_predmeta,indeks,datum,exam_info)

@app.delete("/exams/{sifra_predmeta}/{indeks}/{datum}")
async def delete_subject(sifra_predmeta:str,indeks:str,datum:str):
    return exam_service.delete(sifra_predmeta,indeks,datum)

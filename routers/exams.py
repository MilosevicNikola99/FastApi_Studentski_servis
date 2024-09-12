from fastapi import FastAPI, APIRouter, Depends

from ..services.exam_services import ExamService
from ..schemas.schemas import Exam
from ..schemas.schemas import ExamInfo

router = APIRouter()


exam_service = ExamService("resources/exams.json")



@router.get("/exams",tags=["exams"])
async def get_exams(sifra_predmeta:str | None = None,indeks:str | None = None):
    if sifra_predmeta and indeks:
        return exam_service.get_by_sifra_indeks(sifra_predmeta, indeks)
    elif sifra_predmeta:
        return exam_service.get_by_sifra_predmeta(sifra_predmeta)
    elif indeks:
        return exam_service.get_by_indeks(indeks)
    return exam_service.get_all_exams()

@router.get("/exams/statistics/{indeks}",tags=["exams"])
async def get_statistics(indeks: str):
    return exam_service.calculate_statistics(indeks)

@router.post("/exams/{sifra_predmeta}/{indeks}",tags=["exams"])
async def create_subject(sifra_predmeta:str,indeks:str ,exam_info : ExamInfo):
    exam_info = exam_info.model_dump()
    exam = Exam(datum= exam_info["datum"],ocena=exam_info["ocena"],polozen=exam_info["polozen"],indeks=indeks,sifra_predmeta=sifra_predmeta)
    exam_service.create(exam.model_dump())
    print(exam.model_dump())
    return exam.model_dump()

@router.put("/exams/{sifra_predmeta}/{indeks}/{datum}",tags=["exams"])
async def update_subject(sifra_predmeta:str,indeks:str,datum:str,exam_info : ExamInfo):
    return exam_service.update(sifra_predmeta,indeks,datum,exam_info.model_dump())

@router.delete("/exams/{sifra_predmeta}/{indeks}/{datum}",tags=["exams"])
async def delete_subject(sifra_predmeta:str,indeks:str,datum:str):
    return exam_service.delete(sifra_predmeta,indeks,datum)


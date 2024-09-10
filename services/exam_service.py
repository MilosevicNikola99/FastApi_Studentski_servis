from repositories.exam_repository import ExamRepository
from fastapi import HTTPException

class ExamService():
    def __init__(self,path):
        self.repository = ExamRepository(path)

    def create(self, exam):
        if self.repository.exam_exists(exam["sifra_predmeta"]):
            raise HTTPException(status_code=400, detail="Exam already exists")
        self.repository.add_exam(exam)

    def get_by_code(self, sifra_predmeta: str):
        for exam in self.repository.exams:
            if exam["sifra_predmeta"] == sifra_predmeta:
                return exam
        raise HTTPException(status_code=404,detail="Exam not found")

    def update(self, sifra_predmeta:str, exam):

        for exam1 in self.repository.exams:
            if exam1["sifra_predmeta"] == sifra_predmeta:
                exam1["sifra_predmeta"] = exam["sifra_predmeta"]
                exam1["naziv"] = exam["naziv"]
                exam1["espb"] = exam["espb"]
                self.repository.update_exams()
                return self.repository.exams

        raise HTTPException(status_code=404,detail="Exam not found")

    def delete(self, sifra_predmeta: str):
        for exam in self.repository.exams:
            if exam["sifra_predmeta"] == sifra_predmeta:
                self.repository.exams.remove(exam)
                self.repository.update_exams()
                return self.repository.exams

        raise HTTPException(status_code=404 , detail="Exam not found")

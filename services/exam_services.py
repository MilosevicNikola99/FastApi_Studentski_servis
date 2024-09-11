from repositories.exam_repository import ExamRepository
from fastapi import HTTPException

class ExamService():
    def __init__(self,path):
        self.repository = ExamRepository(path)

    def create(self, exam):
        if self.repository.exam_exists(exam["indeks"],exam["sifra_predmeta"],exam["datum"]):
            raise HTTPException(status_code=400,detail="Exam already exists")
        print(exam)
        self.repository.add_exam(exam)


    def get_by_indeks(self, indeks: str):
        exams = []
        for exam in self.repository.exams:
            if exam["indeks"] == indeks:
                exams.append(exam)

        if len(exams) == 0:
            raise HTTPException(status_code=404,detail="Exams not found")
        return exams

    def get_by_sifra_predmeta(self, sifra_predmeta: str):
        print(sifra_predmeta)
        exams = []
        for exam in self.repository.exams:
            if exam["sifra_predmeta"] == "P120":
                exams.append(exam)

        if len(exams) == 0:
            raise HTTPException(status_code=404,detail="Exams not found")

        return exams

    def update(self,indeks:str,sifra_predmeta: str,datum:str, update_exam):
        for exam in self.repository.exams:
            if (exam["indeks"] == indeks and
                exam["sifra_predmeta"] == sifra_predmeta and
                exam["datum"] == datum ):

                exam["ocena"] = update_exam["ocena"]
                exam["polozen"] = True if int(exam["ocena"]) > 5 else False
                self.repository.update_exams()
                return exam

        raise HTTPException(status_code=404,detail="Exam not found")

    def delete(self,sifra_predmeta: str,indeks:str,datum:str):
        print("indeks,sifra i datum: ",indeks,sifra_predmeta,datum)
        for exam in self.repository.exams:
            print(exam)
            print(exam["indeks"] == indeks,exam["indeks"],indeks)
            print(exam["sifra_predmeta"] == sifra_predmeta,exam["sifra_predmeta"],sifra_predmeta)
            print(exam["datum"] == datum,exam["datum"],datum)
            if (exam["indeks"] == indeks and
                exam["sifra_predmeta"] == sifra_predmeta and
                exam["datum"] == datum ):

                self.repository.exams.remove(exam)
                self.repository.update_exams()
                return self.repository.exams

        raise HTTPException(status_code=404,detail="Exam not found")


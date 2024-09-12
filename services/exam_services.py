from ..repositories.exam_repository import ExamRepository
from fastapi import HTTPException

class ExamService():
    def __init__(self,path):
        self.repository = ExamRepository(path)

    def create(self, exam):
        if self.repository.exam_exists(exam["indeks"],exam["sifra_predmeta"],exam["datum"]):
            raise HTTPException(status_code=400,detail="Exam already exists")
        self.repository.add_exam(exam)

    def get_all_exams(self):
        return self.repository.get_exams()

    def get_by_indeks(self, indeks: str):
        exams = []
        for exam in self.repository.exams:
            print(exam["indeks"],indeks)
            if exam["indeks"] == indeks:
                exams.append(exam)

        if len(exams) == 0:
            raise HTTPException(status_code=404,detail="Exams not found")
        return exams

    def get_by_sifra_predmeta(self, sifra_predmeta: str):
        exams = []
        for exam in self.repository.exams:
            if exam["sifra_predmeta"] == sifra_predmeta:
                exams.append(exam)

        if len(exams) == 0:
            raise HTTPException(status_code=404,detail="Exams not found")

        return exams

    def get_by_sifra_indeks(self, sifra_predmeta: str,indeks: str):
        exams = []
        print(sifra_predmeta,indeks)
        for exam in self.repository.exams:
            if exam["sifra_predmeta"] == sifra_predmeta and exam["indeks"] == indeks:
                exams.append(exam)

        if len(exams) == 0:
            raise HTTPException(status_code=404,detail="Exams not found")
        return exams

    def update(self,sifra_predmeta: str,indeks:str,datum:str, update_exam):
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
        for exam in self.repository.exams:
            if (exam["indeks"] == indeks and
                exam["sifra_predmeta"] == sifra_predmeta and
                exam["datum"] == datum ):

                self.repository.exams.remove(exam)
                self.repository.update_exams()
                return self.repository.exams

        raise HTTPException(status_code=404,detail="Exam not found")

    def calculate_statistics(self, indeks):
        polozeni = 0
        nepolozeni = 0
        espb = 0
        for exam in self.repository.exams:
            if (exam["indeks"] == indeks):
                if exam["polozen"]:
                    polozeni += 1
                    espb += 1 #Ovde nemamo pdatke koliko koji predmet nosi espb poena
                else:
                    nepolozeni += 1

        return { "polozio": polozeni,"nije polozio" :nepolozeni, "ukupno espb":espb}


from repositories.subject_repository import SubjectRepository
from fastapi import HTTPException

class SubjectService():
    def __init__(self,path):
        self.repository = SubjectRepository(path)

    def create(self, subject):
        if self.repository.subject_exists(subject["sifra_predmeta"]):
            raise HTTPException(status_code=400, detail="Subject already exists")
        self.repository.add_subject(subject)

    def get_by_code(self, sifra_predmeta: str):
        for subject in self.repository.subjects:
            if subject["sifra_predmeta"] == sifra_predmeta:
                return subject
        raise HTTPException(status_code=404,detail="Subject not found")

    def update(self, sifra_predmeta:str, subject):

        for subject1 in self.repository.subjects:
            if subject1["sifra_predmeta"] == sifra_predmeta:
                subject1["sifra_predmeta"] = subject["sifra_predmeta"]
                subject1["naziv"] = subject["naziv"]
                subject1["espb"] = subject["espb"]
                self.repository.update_subjects()
                return self.repository.subjects

        raise HTTPException(status_code=404,detail="Subject not found")

    def delete(self, sifra_predmeta: str):
        for subject in self.repository.subjects:
            if subject["sifra_predmeta"] == sifra_predmeta:
                self.repository.subjects.remove(subject)
                self.repository.update_subjects()
                return self.repository.subjects

        raise HTTPException(status_code=404 , detail="Subject not found")

from pydantic import BaseModel

class StudentIndeks(BaseModel):
    indeks: str

class Student(StudentIndeks):
    id: int
    name: str | None = None
    prezime: str | None = None


class SubjectCode(BaseModel):
    sifra_predmeta: str

class Subject(SubjectCode):
    naziv: str | None = None
    espb: int | None = None


class ExamInfo(BaseModel):
    datum : str | None = None
    ocena : int | None = None
    polozen: bool | None = None

class Exam(ExamInfo,StudentIndeks,SubjectCode):
    pass
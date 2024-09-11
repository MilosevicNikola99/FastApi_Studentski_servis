from pydantic import BaseModel

class StudentIndeks(BaseModel):
    indeks: str

class Student(StudentIndeks):
    id: int
    name: str | None = None
    prezime: str | None = None


class CourseCode(BaseModel):
    sifra_predmeta: str

class Course(CourseCode):
    naziv: str | None = None
    espb: int | None = None


class ExamInfo(BaseModel):
    datum : str | None = None
    ocena : int | None = None
    polozen: bool | None = None

class Exam(ExamInfo,StudentIndeks,CourseCode):
    pass

from repositories.student_repository import StudentRepositoriy
from fastapi import HTTPException

class StudentService:
    def __init__(self,path):
        self.repository = StudentRepositoriy(path)

    def create(self, student):
        if self.repository.student_exists(student["id"]):
            raise HTTPException(status_code=400,detail="Student already exists")
        self.repository.add_student(student)

    def get_by_id(self, id: int):
        for student in self.repository.students:
            if student["id"] == id:
                return student

        raise HTTPException(status_code=404)

    def update(self, id, student):

        for student1 in self.repository.students:
            if student1["id"] == id:
                student1["name"] = student.name
                student1["prezime"] = student.prezime
                student1["indeks"] = student.indeks
                self.repository.update_students()
                return self.repository.students

            raise HTTPException(status_code=404,detail="Student not found")

    def delete(self, id):
        for student1 in self.repository.students:
            if student1["id"] == id:
                self.repository.students.remove(student1)
                self.repository.update_students()
                return self.repository.students

        raise HTTPException(status_code=404 , detail="Student not found")

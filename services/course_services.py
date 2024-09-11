from repositories.course_repository import CourseRepository
from fastapi import HTTPException

class CourseService():
    def __init__(self,path):
        self.repository = CourseRepository(path)

    def create(self, course):
        if self.repository.course_exists(course["sifra_predmeta"]):
            raise HTTPException(status_code=400, detail="Course already exists")
        self.repository.add_course(course)

    def get_by_code(self, sifra_predmeta: str):
        for course in self.repository.courses:
            if course["sifra_predmeta"] == sifra_predmeta:
                return course
        raise HTTPException(status_code=404,detail="Course not found")

    def update(self, sifra_predmeta:str, course):

        for course1 in self.repository.courses:
            if course1["sifra_predmeta"] == sifra_predmeta:
                course1["sifra_predmeta"] = course["sifra_predmeta"]
                course1["naziv"] = course["naziv"]
                course1["espb"] = course["espb"]
                self.repository.update_courses()
                return self.repository.courses

        raise HTTPException(status_code=404,detail="Course not found")

    def delete(self, sifra_predmeta: str):
        for course in self.repository.courses:
            if course["sifra_predmeta"] == sifra_predmeta:
                self.repository.courses.remove(course)
                self.repository.update_courses()
                return self.repository.courses

        raise HTTPException(status_code=404 , detail="Course not found")

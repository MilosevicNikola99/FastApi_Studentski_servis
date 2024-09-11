import json


class CourseRepository():
    def __init__(self,path):
        self.path = path
        self.courses = self.read_courses()

    def read_courses(self):
        with open(self.path , "r") as f:
            return  json.load(f)

    def add_course(self,course):
        self.courses.append(course)
        with open(self.path, "r+") as f:
            f.seek(0)
            f.write(json.dumps(self.courses))

    def update_courses(self):
        with open(self.path, "r+") as f:
            f.seek(0)
            f.truncate()
            f.write(json.dumps(self.courses))

    def course_exists(self,sifra_predmeta):
        for course in self.courses:
            if course['sifra_predmeta'] == sifra_predmeta:
                return True
        return False

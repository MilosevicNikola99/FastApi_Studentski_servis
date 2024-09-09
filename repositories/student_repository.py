import json


class StudentRepositoriy():
    def __init__(self,path):
        self.path = path
        self.students = self.read_students(path)

    def read_students(self,path):
        with open(path , "r") as f:
            self.students = json.load(f)
            return self.students

    def add_student(self,student):
        self.students.append(student)
        with open(self.path, "r+") as f:
            f.seek(0)
            f.write(json.dumps(self.students))

    def update_students(self):
        with open(self.path, "r+") as f:
            f.seek(0)
            f.truncate()
            f.write(json.dumps(self.students))

    def delete_student(self,d_student):
        for student in self.students:
            if student['id'] == d_student['id']:
                self.students.remove(student)
                self.update_students()
    def student_exists(self,id):
        for student in self.students:
            if student['id'] == id:
                return True
        return False




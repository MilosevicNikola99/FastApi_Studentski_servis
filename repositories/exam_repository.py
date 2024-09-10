import json


class ExamRepository():
    def __init__(self,path):
        self.path = path
        self.exams = self.read_exams(path)

    def read_exams(self,path):
        with open(path , "r") as f:
            self.exams = json.load(f)
            return self.exams

    def add_exam(self,exam):
        self.exams.append(exam)
        with open(self.path, "r+") as f:
            f.seek(0)
            f.write(json.dumps(self.exams))

    def update_exams(self):
        with open(self.path, "r+") as f:
            f.seek(0)
            f.truncate()
            f.write(json.dumps(self.exams))

    def delete_exam(self,d_exam):
        for exam in self.exams:
            if exam['sifra_predmeta'] == d_exam['sifra_predmeta']:
                self.exams.remove(exam)
                self.update_exams()

    def exam_exists(self,sifra_predmeta):
        for exam in self.exams:
            if exam['sifra_predmeta'] == sifra_predmeta:
                return True
        return False

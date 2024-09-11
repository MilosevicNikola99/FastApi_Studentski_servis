import json

class ExamRepository():
    def __init__(self,path):
        self.path = path
        self.exams = self.read_exams()

    def read_exams(self):
        with open(self.path , "r") as f:
            return json.load(f)

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
            if (exam['indeks'] == d_exam['indeks'] and
                exam['sifra_predmeta'] == d_exam['sifra_predmeta'] and
                exam['datum'] == d_exam['datume']):
                self.exams.remove(exam)
                self.update_exams()

    def exam_exists(self,indeks,sifra_predmeta,datum):
        for exam in self.exams:
            if (exam['indeks'] == indeks and
                exam['sifra_predmeta'] == sifra_predmeta and
                exam['datum'] == datum):
                return True
        return False



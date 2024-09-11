import json


class SubjectRepository():
    def __init__(self,path):
        self.path = path
        self.subjects = self.read_subjects()

    def read_subjects(self):
        with open(self.path , "r") as f:
            return  json.load(f)

    def add_subject(self,subject):
        self.subjects.append(subject)
        with open(self.path, "r+") as f:
            f.seek(0)
            f.write(json.dumps(self.subjects))

    def update_subjects(self):
        with open(self.path, "r+") as f:
            f.seek(0)
            f.truncate()
            f.write(json.dumps(self.subjects))

    def subject_exists(self,sifra_predmeta):
        for subject in self.subjects:
            if subject['sifra_predmeta'] == sifra_predmeta:
                return True
        return False

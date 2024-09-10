import json


class SubjectRepository():
    def __init__(self,path):
        self.path = path
        self.subjects = self.read_subjects(path)

    def read_subjects(self,path):
        with open(path , "r") as f:
            self.subjects = json.load(f)
            return self.subjects

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

    def delete_subject(self,d_subject):
        for subject in self.subjects:
            if subject['sifra_predmeta'] == d_subject['sifra_predmeta']:
                self.subjects.remove(subject)
                self.update_subjects()

    def subject_exists(self,sifra_predmeta):
        for subject in self.subjects:
            if subject['sifra_predmeta'] == sifra_predmeta:
                return True
        return False

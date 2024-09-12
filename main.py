from fastapi import FastAPI
from .routers import exams,students,courses

e = exams.get_exam_service()
s = students.get_student_service()
c = courses.get_course_service()

import uvicorn
app = FastAPI()

app.include_router(exams.router)
app.include_router(students.router)
app.include_router(courses.router)

@app.get("/espb/{indeks}",tags=["statistics"])
async def get_indeks(indeks:str):
    espb = 0
    polozeni_ispiti = e.get_by_indeks(indeks)
    for ispit in polozeni_ispiti:
        espb += c.get_by_code(ispit["sifra_predmeta"])["espb"]
    return {"Ukupno espb" : espb}

@app.get("/statistics/{indeks}",tags=["statistics"])
async def get_statistics(indeks: str):
    return e.calculate_statistics(indeks)


# if __name__ == "__main__":
#     uvicorn.run("main:app", port=8001, reload=True, log_config=None)
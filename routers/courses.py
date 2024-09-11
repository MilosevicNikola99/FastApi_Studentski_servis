from fastapi import FastAPI
from schemas.schemas import Course
from services.course_services import CourseService
app = FastAPI()



course_service = CourseService("resources/course.json")

@app.post("/courses")
async def create_course(course: Course):
    course_service.create(course.model_dump())
    return course.model_dump()

@app.get("/courses/{course_code}")
async def get_course(course_code: str):
    return course_service.get_by_code(course_code)

@app.put("/courses/{course_code}")
async def update_course(course_code: str,course: Course):
    return course_service.update(course_code,course.model_dump())

@app.delete("/courses/{course_code}")
async def delete_course(course_code: str):
    return course_service.delete(course_code)


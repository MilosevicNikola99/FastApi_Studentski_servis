from fastapi import FastAPI , APIRouter
from ..schemas.schemas import Course
from ..services.course_services import CourseService


router = APIRouter()

course_service = CourseService("resources/course.json")

@router.post("/courses",tags=["courses"])
async def create_course(course: Course):
    course_service.create(course.model_dump())
    return course.model_dump()

@router.get("/courses/{course_code}",tags=["courses"])
async def get_course(course_code: str):
    return course_service.get_by_code(course_code)

@router.put("/courses/{course_code}",tags=["courses"])
async def update_course(course_code: str,course: Course):
    return course_service.update(course_code,course.model_dump())

@router.delete("/courses/{course_code}",tags=["courses"])
async def delete_course(course_code: str):
    return course_service.delete(course_code)

def get_course_service():
    return course_service
from fastapi import FastAPI
from .routers import exams,students,courses

import uvicorn
app = FastAPI()

app.include_router(exams.router)
app.include_router(students.router)
app.include_router(courses.router)

@app.get("/")
async def root():
    return {"Hello": "World"}

# if __name__ == "__main__":
#     uvicorn.run("main:app", port=8001, reload=True, log_config=None)
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


# Mô hình dữ liệu gửi vào API
class Student(BaseModel):
    id: int
    name: str


# API GET đơn giản
@app.get("/api/hello")
def hello():
    return {"message": "Xin chào từ Web API!"}


# API GET có params
@app.get("/api/sum")
def calc_sum(a: int, b: int):
    return {"result": a + b}


# API POST nhận JSON
@app.post("/api/student")
def create_student(student: Student):
    return {
        "status": "received",
        "student": student,
    }

# استيراد من المكتبات 
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()


class TodoItem(BaseModel):
    title: str
    description: str = "No description"  
    done: bool = False

all_of_my_todos = []  # هنا نحفظ الأشياء

origins = ["http://localhost:8000", "http://127.0.0.1:8000"]  # هذه الروابط التابعه للمشروع 

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,  # هذا مهم جدا
    allow_methods=["*"],
    allow_headers=["*"],  # نفس الشيء هنا
)

@app.post("/todos/")  #  مكان لوضع الأشياء الجديد
def create_a_todo(todo: TodoItem):
    all_of_my_todos.append(todo)  # الأشياء تروح هنا
    return todo  

@app.get("/todos/") 
def get_all_todos():
    return all_of_my_todos

@app.get("/todos/{id_of_todo}")
def get_a_single_todo(id_of_todo: int):
    if id_of_todo >= len(all_of_my_todos):  
        return {"error": "not found!! "}
    return all_of_my_todos[id_of_todo]

@app.put("/todos/{id_of_todo}")  
def change_a_todo(id_of_todo: int, todo: TodoItem):
    if id_of_todo >= len(all_of_my_todos):  
        return {"error": "not found!! "}
    all_of_my_todos[id_of_todo] = todo  
    return todo 

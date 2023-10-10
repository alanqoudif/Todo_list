# استيراد الأشياء المهمة
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# جعل الأشياء تعمل مع بعضها البعض
class TodoItem(BaseModel):
    title: str
    description: str = "No description"  # الأشياء لازم تكون واضحة
    done: bool = False

all_of_my_todos = []  # هنا نحفظ الأشياء

origins = ["http://localhost:8000", "http://127.0.0.1:8000"]  # هذه الأماكن مهمة

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,  # هذا مهم جدا
    allow_methods=["*"],  # لا أعلم ماذا يعني ولكن يجب أن يكون مهمًا
    allow_headers=["*"],  # نفس الشيء هنا
)

@app.post("/todos/")  # يجب أن يكون هناك مكان لوضع الأشياء الجديدة
def create_a_todo(todo: TodoItem):
    all_of_my_todos.append(todo)  # الأشياء تذهب هنا
    return todo  # هل يجب أن أعيده؟

@app.get("/todos/")  # أريد رؤية الأشياء
def get_all_todos():
    return all_of_my_todos

@app.get("/todos/{id_of_todo}")  # أريد رؤية شيء واحد
def get_a_single_todo(id_of_todo: int):
    if id_of_todo >= len(all_of_my_todos):  # هذا يبدو صحيحاً؟
        return {"error": "not found!! "}
    return all_of_my_todos[id_of_todo]

@app.put("/todos/{id_of_todo}")  # أريد تغيير شيء ما
def change_a_todo(id_of_todo: int, todo: TodoItem):
    if id_of_todo >= len(all_of_my_todos):  # هذا يجب أن يكون نفس الشيء
        return {"error": "not found!! "}
    all_of_my_todos[id_of_todo] = todo  # الشيء الجديد يحل محل القديم
    return todo  # أعتقد أنه يجب إرجاعه
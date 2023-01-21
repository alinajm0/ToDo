
from ninja import NinjaAPI, Schema
from datetime import date
from typing import List
from django.shortcuts import get_object_or_404
from todo_list.models import task





api = NinjaAPI()

# api = NinjaAPI()
# @api.get("/add")
# def add(request, a:int, b:int):
#     return {'result': a + b}

# @api.get("/math")
# def math(request, a: int, b: int):
#     return {"add": a + b, "multiply": a * b}

# @api.get("/math/{a}and{b}")
# def math(request, a: int, b: int):
#     return {"add": a + b, "multiply": a * b}


# @api.get("/hello")
# def hello(request, name : str ='World!'):
#     return f"Hello {name}"

# class HelloSchema(Schema):
#     name :str = 'World!'

# @api.post('/hello')
# def hello(request, data : HelloSchema):
#     return f'hello {data.name}'


class ToDo_list(Schema):
    id :int
    title:str
    Desc:str
    Date: date
    

# class EmployeeOut(Schema):
#     id: int
#     first_name: str
#     last_name: str
#     department_id: int = None
#     birthdate: date = None


@api.post("/todo_list")
def create_task(request, t: ToDo_list):
    t1 = task.objects.create(**t.dict())
    return {"id": t1.id}


@api.get("/todo_list/{task_id}", response = ToDo_list)
def get_task(request, task_id: int):
    t = get_object_or_404(task, id=task_id)
    return t



@api.put("/todo_list/{task_id}")
def update_task(request, task_id: int, t: ToDo_list):
    t1 = get_object_or_404(task, id=task_id)
    for attr, value in t.dict().items():
        setattr(t1, attr, value)
    t1.save()
    return {"success": True}


@api.delete("/todo_list/{task_id}")
def delete_task(request, task_id: int):
    t1 = get_object_or_404(task, id=task_id)
    t1.delete()
    return {"success": True}
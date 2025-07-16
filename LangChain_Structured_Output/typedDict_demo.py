from typing import TypedDict

class Person(TypedDict):
    name: str
    age: int
    is_student: bool
    email: str

p1: Person = {
    "name": "amjad",   
    "age": 30,
    "is_student": False,
    "email": "amjad@example.com"
}

print(p1)

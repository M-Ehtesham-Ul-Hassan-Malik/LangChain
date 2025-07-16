from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class Student(BaseModel):
    name: str
    age: Optional[int] = None
    grade: str
    email: Optional[EmailStr] = None  # Using EmailStr for email validation
    cgpa: float = Field(..., ge=0.0, le=4.0, description='Cumulative Grade Point Average of the student')  # CGPA must be between 0.0 and 4.0

new_student = {
    'name' : "Fatima Zahra",
    # 'age' : 7, # since it is optional, we can omit it
    'grade' : "A", # Corrected to a valid string
    # 'grade' : 3 #  Uncommenting this line will raise a validation error
    'email' : "fatima.zahra@fast.com",
    'cgpa' : 3.8  # CGPA must be between 0.0 and 4.0
}

student = Student(**new_student)



print(student)

student_json = student.model_dump_json()
print(student_json)
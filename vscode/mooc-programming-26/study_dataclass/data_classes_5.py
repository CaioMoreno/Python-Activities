from dataclasses import dataclass, field

@dataclass
class NewPerson:
    name: str
    age: int 
    city: str 

@dataclass
class Student(NewPerson):
    grade: int
    subjects: list

p1 = Student("caio", 25, 10, 75, ["math", "portuguese"])
print(p1)



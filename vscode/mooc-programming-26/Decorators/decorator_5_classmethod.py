data = [{"name": "caio", "age": 25, "roll_no": 2142}, {"name": "lu", "age": 22, "roll_no": 5256}, {"name": "sasuke", "age": 110, "roll_no": 1111}]
class Student:
    def __init__(self, name, age, roll_no):
        self.name = name
        self.age = age
        self.roll_no = roll_no

    @classmethod
    def from_dicts(cls, data):
        students = []
        for s in data:
            student = cls(s["name"], s["age"], s["roll_no"]) 
            students.append(student)
        return students

students = Student.from_dicts(data)
for i in students:
    print(f"{i.name} {i.age} {i.roll_no}")

from dataclasses import dataclass

@dataclass
class NewPerson:
    name: str
    age: int
    city: str

p1 = NewPerson("caio", 25, "BH")
p2 = NewPerson("caio", 25, "BH")

print(p1)
print(p1 == p2)

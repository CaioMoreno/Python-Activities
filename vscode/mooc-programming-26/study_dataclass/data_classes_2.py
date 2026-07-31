from dataclasses import dataclass

@dataclass(order=True, frozen=True, unsafe_hash=True)
class NewPerson:
    name: str
    age: int
    city: str

p1 = NewPerson("caio", 25, "BH")
p2 = NewPerson("caio", 25, "BH")
#init
print(p1.name, p1.age, p1.city)
#repr
print(p1)
#eq
print(p1 == p2)
#order
print(p1 > p2)
#unsafe_hash: hash doesnt work for mutable varialbes but this makes them work
print(hash(p1))
#frozen: it doesn't let change
p1.city = "M"

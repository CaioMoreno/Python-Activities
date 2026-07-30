from dataclasses import dataclass, asdict,  astuple
import json

@dataclass
class Address:
    lat: float
    lng: float
    city: str
    country: str

@dataclass
class NewPerson:
    name: str
    age: int 
    addr: Address 

a = Address(54.66, 102.30, "BH", "Brazil")
p = NewPerson("caio", 25, a)

print(p)
print(asdict(p))
print(json.dumps(asdict(p)))
print(astuple(p))




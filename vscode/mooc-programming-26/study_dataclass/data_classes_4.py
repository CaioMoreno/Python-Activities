from dataclasses import dataclass, field

@dataclass()
class NewPerson:
    name: str
    age: int 
    points: int 
    passed: bool = field(init=False)

    def __post_init__(self):
        if self.points >= 6:
            self.passed = True
        else:
            self.passed = False

p1 = NewPerson("caio", 25, 10)
print(p1)



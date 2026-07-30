from dataclasses import dataclass, field

@dataclass(unsafe_hash=True)
class NewPerson:
    name: str

    #init: if a object is not given it gives a default value
    #repr: doesnt print the object
    #hash: if not want a variable in your hash function
    age: int = field(init=False, default=25, repr=False, hash=False)

    #default: gets a default value only works for the last object of the class
    #points: int = field(default=0)
    #default_factory: very useful to get the default from a function that takes no arguments
    #compare: it won't compare this method
    #metadata: add some data for the variable
    points: int = field(default_factory=get_default_points, compare=False, metadata={"format": "score"})

p1 = NewPerson("caio", 25)
#p1 = NewPerson("caio", 25, 10)
p2 = NewPerson("caio", 26)

print(p1.__dataclass_fields__)
print(p1)
print(hash(p1))
print(p1 == p2)
print(p1.__dataclass_fields__["points"].metadata["format"])

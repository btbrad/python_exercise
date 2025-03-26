from dataclasses import dataclass, field


@dataclass
class Person:
    name: str
    age: int
    gender: bool = field(default=False, repr=False)


p = Person('bt', 20)
print(p)









def foo(par) -> str: 
    if par >= 87:
        return "hola"
    elif par == [(1,'hi')]:
        a = True
   
# comment
n, s = 91, "hola"
li = [[3, "chau", True, None, (2, 3), int], 1]
di = {"name": "John"}
f = foo(n)

for x in range(len(li)):
    print(li[x])

from dataclasses import dataclass

class Animal:
    def __init__(self) -> None:
        pass

@dataclass
class Persona:
    name: str
    age: int

    def saludo(self):
        print(f"Hola {self.name}, tenés {self.age} años")

    def __str__(self) -> str:
        return f"{self.name} tiene {self.age} años"

abecedario = "abcdefghijklmnopqrstuvwxyz"

ABECEDARIO = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

print("oO08 iIlL1 g9qCGQ ~-+=>")
# â é ù ï ø ç Ã Ē Æ œ

p = Persona("Paul", 57)
p.saludo()
print(p)
print(f"\N{Sauropod}")

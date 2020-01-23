# magic method are python method with a double underscore before and after
# the function name. 
# ex. __init__, __repr__, __len__
from copy import copy
class Human:
    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        self.age = age
    
    def __len__(self):
        return self.age
    
    def __repr__(self):
        return f"This human is named {self.first} {self.last}"
    
    def __add__(self, other):
        if isinstance(other, Human):
            return Human(first='newborn', last=self.last, age=0)
        else:
            raise TypeError("Must add a human")
    
    def __mul__(self, other):
        if isinstance(other, int):
            # copy function creates copy of this object, instead of an identical copy
            return [copy(self) for i in range(other)]
        else:
            raise TypeError("Must be an int")

dallas = Human('dallas', 'mcgroarty', 60)
bob = Human('bob', 'jones', 45)
print(len(dallas))
print(dallas)

print(dallas + bob)
peeps = dallas * 2
peeps[0].first = 'Tom'
print(peeps) 
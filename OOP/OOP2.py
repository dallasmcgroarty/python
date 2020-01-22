# inheritance - key feature pf OOP is the ability to define a class which inherits
# from another class (a "base" or "parent" class)

# inheritance works by passing the parent class as an argument to the definition of
# a child class

class Animal:
    cool = True

    def make_sound(self, sound):
        print(f"this animal says {sound}")

class Cat(Animal):
    pass

a = Animal()
a.make_sound("yohoo")

blue = Cat()
blue.make_sound("meow")

print(blue.cool, Animal.cool, Cat.cool)

# is instance return true if the type is the same else returns false
print(isinstance(blue, Cat))

#********** 
# Properties
#**********
class Human:
    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        if age >= 0:
            self._age = age
        else:
            self._age = 0
    
    # def get_age(self):
    #     return self._age
    
    # def set_age(self, new_age):
    #     if new_age >= 0:
    #         self._age = new_age
    #     else:
    #         self._age = 0

# property method lets you create a method that acts like an attribute (use as getter)
    @property
    def age(self):
        return self._age

# create a setter for that property
    @age.setter
    def age(self, value):
        if value >= 0:
            self._age = value
        else:
            raise ValueError("age cannot be negative")

    @property
    def full_name(self):
        return f"{self.first} {self.last}"
    
    @full_name.setter
    def full_name(self, name):
        self.first, self.last = name.split(" ")

jane = Human("Jane","Goodal", 30)
# print(jane.get_age())
# jane.set_age(45)
# print(jane.get_age())

print(jane.age)
jane.age = 23
print(jane.age)
print(jane.full_name)
jane.full_name = "Tommy Bob"
print(jane.full_name)


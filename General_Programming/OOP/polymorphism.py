# polymorphism - a key principle in OOP is the idea that an object cant take on 
# many forms

# examples:
# 1. the same class method works in a similar way for different classes
# Cat.speak() # moew
# Dog.speak() # woof
# Human.speak() # yo

# common way to do this is to have a method in a base (or parent) class that
# is overridden by a subclass. aka. method overriding
class Animal():
    def speak(self):
        raise NotImplementedError("Subclass needs to implement this method")
class Dog(Animal):
    def speak(self):
        return "woof"
class Cat(Animal):
    def speak(self):
        return "meow"

dog = Dog()
cat = Cat()
print(dog.speak())
print(cat.speak())    

# 2. the same operation works for different kinds of objects
sample_list = [1,2,3]
sample_tuple = (1,2,3)
sample_string = "awesome"

len(sample_list)
len(sample_tuple)
len(sample_string)
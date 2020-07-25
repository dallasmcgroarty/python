class User:
    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        self.age = age
    def full_name(self):
        return f"{self.first} {self.last}"

    def user_age(self):
        return f"{self.first} is {self.age} years old"

    def initials(self):
        return f"{self.first[0]}.{self.last[0]}."

    def likes(self, thing):
        return f"{self.first} likes {thing}"
    
    def is_senior(self):
        return self.age >= 65

    def birthday(self):
        self.age += 1
        return f"Happy {self.age}th, {self.first}!"

user1 = User('Tom', 'Jones', 45)
user2 = User('Jerry', 'Bones', 67)
print(user2.full_name())
print(user1.user_age())

print(user1.likes('Candy'))

print(user1.initials())

print(user2.is_senior())

print(user1.birthday())
print(user1.age)
# No private or public keywords in python
# everything method or attribute is public
# developers can use a single _ before a variable to show
# that that method or variable is supposed to be private

# double __ used for name mangling and inheritance, keeps it unique
# __example__ used for python specific methods
class Person:
    def __init__(self):
        self.name = 'tony'
        self._secret = 'hi!'
        self.__msg = 'i like turtles'
        self.__lol = 'hahaha'
    def check_secret(self, guess):
        if guess == self._secret:
            #let them see it
            pass

p = Person()
print(p.name)
print(p._secret)
print(dir(p))
print(p._Person__msg)
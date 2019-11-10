# class methods are methods (with the @ decorator)
# that are not concerned with instances, but the class itself
class User:
    # class attribute below
    active_users = 0

    @classmethod
    def display_active_users(cls):
        return f"There are currently {cls.active_users} active users"

    @classmethod
    def from_string(cls, data_str):
        first, last, age = data_str.replace(' ','').split(',')
        return cls(first, last, age)

    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        self.age = age
        # add one for every initialized user
        User.active_users += 1

    # repr method changes whats printed/represented for an object
    def __repr__(self):
        return f"{self.first} is {self.age}"
        
    def logout(self):
        User.active_users -= 1
        return f"{self.first} has logged out"

    def full_name(self):
        return f"{self.first} {self.last}"

    def user_age(self):
        return f"{self.first} is {self.age} years old"

    def initials(self):
        return f"{self.first[0]}.{self.last[0]}."

    def likes(self, thing):
        return f"{self.first} likes {thing}"
    
user1 = User('tom','Jones', 34)
user2 = User('Bob', 'Bingle', 26)
print(User.display_active_users())
user1 = User('tom','Jones', 34)
user2 = User('Bob', 'Bingle', 26)
print(User.display_active_users())

user3 = User.from_string("Tom, Bones, 89")
print(user3.full_name())

# repr method changes whats printed/represented for an object
print(user2)
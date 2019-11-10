class User:
    # class attribute below
    active_users = 0

    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        self.age = age
        # add one for every initialized user
        User.active_users += 1
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

print(User.active_users)

user1 = User('tom','Jones', 34)
user2 = User('Bob', 'Bingle', 26)

print(User.active_users)

print(user1.logout())
print(User.active_users)
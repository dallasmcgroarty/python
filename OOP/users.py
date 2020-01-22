# class methods are methods (with the @ decorator)
# that are not concerned with instances, but the class itself

#cls is short for class
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
    
    def birthday(self):
        self.age += 1
        return f"Happy {self.age}th birthday, {self.first}"

# class moderators inherit from user
class Moderator(User):
    total_mods = 0

    def __init__(self, first, last, age, community):
        super().__init__(first, last, age)
        self.community = community
        Moderator.total_mods += 1
    
    @classmethod
    def display_active_mods(cls):
        return f"There are currently {cls.total_mods} active moderators"

    def remove_post(self):
        return f"{self.full_name()} removed a post from the {self.community} community"

print(User.display_active_users())
u1 = User("Tom","Garcia", 24)
print(User.display_active_users())
jasmine = Moderator("Jasmine", "O'Connor", 34, "Piano")
jasmine1 = Moderator("Jasmine", "O'Connor", 34, "Piano")
print(jasmine.full_name())
print(jasmine.community)
print(User.display_active_users())
print(Moderator.display_active_mods())
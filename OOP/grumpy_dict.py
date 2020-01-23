# overriding dictionary object in python
# using magic methods we can override how a dictionary functions
# this can also be applied to other objects as well

class grumpyDict(dict):
    def __repr__(self):
        print("None of Your Business")
        return super().__repr__()
    
    def __missing__(self, key):
        print(f"You Want {key}? Well It Aint Here!")
    
    def __setitem__(self, key, value):
        print("You want to change the dictionary?")
        print("Okay fine!")
        super().__setitem__(key, value)

data = grumpyDict({"first":"Tom", "animal": "cat"})
print(data)
data['city'] = 'Tokyo'
print(data)
data['city'] = 'SF'
print(data)
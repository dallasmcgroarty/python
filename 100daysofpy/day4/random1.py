import random
import my_module

# generate random int from range
random_int = random.randint(1, 10)
print(random_int)

# importing custom module
print(my_module.pi)

# random float between 0 and 1
random_float = random.random()
print(random_float)

# random float between 0 and 4
random_float = random.random() * 5
print(random_float)
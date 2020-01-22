# polymorphism - a key principle in OOP is the idea that an object cant take on 
# many forms

# examples:
# 1. the same class method works in a similar way for different classes
# Cat.speak() # moew
# Dog.speak() # woof
# Human.speak() # yo

# 2. the same operation works for different kinds of objects
sample_list = [1,2,3]
sample_tuple = (1,2,3)
sample_string = "awesome"

len(sample_list)
len(sample_tuple)
len(sample_string)
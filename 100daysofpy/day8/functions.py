def greet():
  print('Hello')
  print('How do you do?')

greet()

# functions with parameters

def add(a, b):
  print( a + b)

add(2,3)

# name = parameter
def greet_with_name(name):
  print(f'Hello {name}')
  print(f'How do you do {name}?')

# 'Dallas' = argument
greet_with_name('Dallas')

# function with multiple inputs
def greet_with_name_loc(name, loc):
  print(f'Hello {name}')
  print(f'What is it like in {loc}?')

greet_with_name_loc('Dallas','Texas')



# Define a function called paint_calc()
import math
def paint_calc(height, width, cover):
  cans = math.ceil((height * width) / cover)
  print(f"You'll need {cans} cans of paint.")


test_h = 3 # Height of wall (m)
test_w = 9 # Width of wall (m)
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)

#prime numbe checker
# Write your code below this line 👇
import math

def prime_checker(num):
  is_prime = True

  for i in range(2, int(math.sqrt(num))+1):
    if (num % i == 0):
      is_prime = False

  if is_prime:
    print("It's a prime number.")
  else:
    print("It's not a prime number.")

# Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = 13 # Check this number
prime_checker(n)
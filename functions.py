#functions in python
#dont repeat code
#cleans up code
#can be reused elsewhere

def say_hi():
    print('Hi!')
say_hi()

print()

#return values from functions
def say_hi2():
    return 'Hi!'
greeting = say_hi2()
print(greeting)

print()
#create function that returns list of even numbers from 1 to 50 (not including 50)
def generate_evens():
    return [num for num in range(1,50) if num % 2 == 0]
print(generate_evens())
print()

#functions that take parameters
def square(num):
    return num * num
print(square(2))
print()

def happy_birthday(name):
    print(f"Happy Birthday {name}")
happy_birthday('Tom')
print()

def print_full_name(first, last):
    return(f'Your full name is {first} {last}')
print(print_full_name('Dallas','McGroarty'))

print()
#take a string and uppercase it and add a ! at the end
def yell(word):
    return word.upper() + "!"
print(yell('i like eggs'))

# Default parameters, power is defaulted to 2 if no value entered
def exponent(num, power=2):
    return num ** power

print(exponent(2,3))
print(exponent(3,2))
print(exponent(7))

def add(a,b):
    return a + b

def subtract(a,b):
    return a - b

# can have default parameters or parameters in general be functions
def math(a,b,fn=add):
    return fn(a,b)

print(math(2,2))
print(math(2,2,subtract))
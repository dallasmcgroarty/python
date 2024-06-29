# Calculator
from art import logo

# add
def add(a, b):
  return a + b

# subtract
def subtract(a, b):
  return a - b

# multiply
def multiply(a, b):
  return a * b

# divide
def divide(a, b):
  return a / b

# operation dict holding key and function operation
operations = {
  '+': add,
  '-': subtract,
  '*': multiply,
  '/': divide
}

print(logo)
num1 = float(input('What\'s the first number? '))

for key in operations:
  print(key)

again = True
curCalc = num1
lastNum = num1
while again:
  chose_op = input('Pick an operation: ')

  nextNum = float(input('What\'s the next number? '))

  answer = operations[chose_op](lastNum, nextNum)

  print(f'{lastNum} {chose_op} {nextNum} = {answer}')

  lastNum = answer

  go_again = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to exit: ")

  if go_again == 'y':
    again = True
  else:
    again = False

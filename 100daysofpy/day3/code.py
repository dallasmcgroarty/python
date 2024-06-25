## conditionals
height = int(input('What is your height in cm? '))

if height >= 120:
  print('you may ride this ride')
else: 
  print('you may not ride this ride')

# nested conditionals

print(1999 % 4)

# check leap year
year = int(input())

if year % 4 == 0:
  if year % 100 == 0:
    if year % 400 == 0:
      print("Leap year")
    else:
      print("Not leap year")
  else:
    print("Leap year")
else:
  print("Not leap year")

## pizza
print("Thank you for choosing Python Pizza Deliveries!")
size = input().lower() # What size pizza do you want? S, M, or L
add_pepperoni = input().lower() # Do you want pepperoni? Y or N
extra_cheese = input().lower() # Do you want extra cheese? Y or N

bill = 0
if size == 's':
  bill += 15
  if add_pepperoni == 'y':
    bill += 2
elif size == 'm':
  bill += 20
  if add_pepperoni == 'y':
    bill += 3
elif size == 'l':
  bill += 25
  if add_pepperoni == 'y':
    bill += 3

if extra_cheese == 'y':
  bill += 1

print(f'Your final bill is: ${bill}.')

## love score
print("The Love Calculator is calculating your score...")
name1 = input() # What is your name?
name2 = input() # What is their name?
# 🚨 Don't change the code above 👆
# Write your code below this line 👇
names = name1 + name2

true_total = 0
for char in 'true':
  true_total += names.lower().count(char)
  
love_total = 0
for char in 'love':
  love_total += names.lower().count(char)

score = int(str(true_total) + str(love_total))
if score < 10 or score > 90:
  print(f'Your score is {str(score)}, you go together like coke and mentos.')
elif score >= 40 and score <= 50:
  print(f'Your score is {str(score)}, you are alright together.')
else:
  print(f'Your score is {str(score)}.')
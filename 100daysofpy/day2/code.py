# python primative types
# int, string, boolean, float

a = '123'
print(str(a))

b = 123
print(int(b))

3 + 5
7 - 3

c = 3 * 2

# division always returns a float
d = c / 3
print(c, d)

# use // to round down float to int
print(c // 3)

# to the power use **
print(2 ** 3)

# python follows PEMDAS priority (), **, *, /, +, -
# mult and div have same priority, prioritizes left side first
# plus and minus have same priority, prioritizes left side first
print(3 * 3 + 3 / 3 - 3) # = 9 + 1 - 3 = 10 - 3 = 7

#BMI
# 1st input: enter height in meters e.g: 1.65
height = 1.65
# 2nd input: enter weight in kilograms e.g: 72
weight = 72
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
bmi = int(weight) / (float(height) * float(height))
print(int(bmi))

# round to specified decimal
round(2.34543, 2)

## F Strings
print(f"The BMI is {bmi} with height: {height}")


### Tip calculator project

#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
bill = float(input("How much is the bill? "))
people = int(input("How many people splitting the bill? "))
tip = int(input("How much is the tip in percent? "))

pay_per_person = round((bill / people) * (tip / 100 + 1), 2)
print(f'{pay_per_person:.2f}')

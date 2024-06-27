# loops in python
fruits = ['apple','peach','pear']

for item in fruits:
  print(item)


# average height
student_heights = [180, 124, 165, 173, 189, 169, 146]

sum = 0
for height in student_heights:
  sum += height
average = round(sum / len(student_heights))
print(f'total height = {sum}')
print(f'number of students = {len(student_heights)}')
print(f'average height = {average}')

# get max
student_scores = [78, 65, 89, 86, 55, 91, 64, 89]

max = student_scores[0]
for score in student_scores:
  if score > max:
    max = score
print(f'The highest score in the class is: {max}')


# range function
# end range is exluded
for num in range(1, 10):
  print(num, end=' ')

print()

total = 0
for num in range(1, 101):
  total += num
print(total)

# sum even numbers from 0 to target
target = int(input()) # Enter a number between 0 and 1000

even_sum = 0
for num in range(0, target + 1):
  if num % 2 == 0:
    even_sum += num
print(even_sum)

# or
even_sum = 0
for num in range(2, target+1, 2):
  even_sum += num
print(even_sum)

#FizzBuzz
for n in range(1, 101):
  if n % 3 == 0 and n % 5 == 0:
    print('FizzBuzz')
  elif n % 3 == 0:
    print('Fizz')
  elif n % 5 == 0:
    print('Buzz')
  else:
    print(n)
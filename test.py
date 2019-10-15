input = "1,2,3,4,5,6,7"

str_list = input.split(',')

sum = 0
for num in str_list:
    sum += int(num)
print(sum)

def temperature(temp):
    if temp <= 30:
        return 'Freezing'
    elif temp <= 50:
        return'Cold'
    elif temp <= 70:
        return 'Mild'
    elif temp <= 90:
        return 'Hot'
    elif temp <= 110:
        return 'Scorching'

print(temperature(40))
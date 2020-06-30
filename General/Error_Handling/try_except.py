# handling errors
# try and excpet blocks

# be specific when using except or raise
# helps to identify the root error

d = {'name':'Ricky'}

def get(d,key):
    try:
        return d[key]
    except KeyError:
        return None

print(get(d,'city'))
print(get(d,'name'))

# else and finally
# else only runs if try doesnt have an error
# finally will always run at the end
while True:
    try:
        num = int(input('Please enter a number:'))
    except ValueError:
        print('Thats not a number!')
    else:
        print('You entered a number!')
        break
    #finally:
        #print('runs no matter what')
print('out of loop')

def divide(a,b):
    try:
        result = a/b
    except ZeroDivisionError:
        print('Cannot divide by zero')
    except TypeError as err:
        print('a and b must be int or float')
        print(err)
    else:
        print(f"{a} divided by {b} is {result}")

divide(1,2)
divide(1,'a')
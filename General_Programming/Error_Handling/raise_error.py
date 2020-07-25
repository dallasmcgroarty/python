# raise your own errors
# call raise someerror('error message')

def colorize(text, color):
    colors = ('cyan','yellow','blue','green','magenta')
    if type(color) is not str:
        raise TypeError('color must be of type str')
    if type(text) is not str:
        raise TypeError("text must be of type str")
    if color not in colors:
        raise ValueError('Color is an invalid color')
    print(f"printed {text} in {color}")

colorize('hello','red')
colorize(2,'red')

raise ValueError('Value is not in range')
# decorators are functions
# they wrap around other functions and enhance them
# decorators are higher order functions
# have the syntax @

def be_polite(fn):
    def wrapper():
        print('What a pleasure to meet you!')
        fn()
        print('Have a great day!')
    return wrapper

@be_polite
def greet():
    print('My name is Dallas')

@be_polite
def rage():
    print('I hate you!')

greet()
rage()
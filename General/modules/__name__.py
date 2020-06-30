# __name__ gives name of the python file
# the file being executed has the name __main__
from before_name import say_sup

def say_hi():
    print(f"HI My __name__ is {__name__}")

say_hi()
say_sup()
import pyfiglet, termcolor


def print_ascii(msg, color):
    allowed_colors = ['blue', 'green', 'yellow', 'red', 'magenta', 'cyan', 'white']
    while color not in allowed_colors:
        print("Please use on of these colors ", allowed_colors)
        color = input("What color would you like to use? ")
    result = pyfiglet.figlet_format(msg)
    result = termcolor.colored(result, color=color)
    print(result)


msg = input("What would you like to print? ")
color = input("What color would you like to use? ")

print_ascii(msg,color)
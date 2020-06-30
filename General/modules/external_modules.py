# python modules hosted somewhere online/on a server
import termcolor, pyfiglet

print(dir(termcolor))

text = termcolor.colored('hello!', color='red', on_color="on_yellow")

print(text)

result = pyfiglet.figlet_format('hi')
print(result)
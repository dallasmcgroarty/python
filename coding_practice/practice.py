# reverse a string different ways
import inspect
# using inspect to print line number of where each function starts
print('---reverse a string---', inspect.getframeinfo(inspect.currentframe()).lineno) 
def rev_str(str1):
    result = ''
    i = len(str1)-1
    while i >= 0:
        result += str1[i]
        i-=1
    return result

def rev_str1(str1):
    result = ''
    for i in range(len(str1),0,-1):
        result += str1[i-1]
    return result

def rev_str2(str1):
    return ''.join(list(reversed(str1)))
    #return str1[::-1]


print(rev_str('hello'))
print(rev_str1('hello'))
print(rev_str2('hello'))
print()
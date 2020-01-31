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

# palindrome
print('---palindrome---', inspect.getframeinfo(inspect.currentframe()).lineno)

def palindrome(str1):
    if len(str1) % 2 != 0:
        return False
    else:
        back = str1[len(str1)//2:]
        if str1[:len(str1)//2] == rev_str(back):
            return True
        else:
            return False

def palindrome1(str1):
    return str1[:len(str1)//2] == str1[len(str1):len(str1)//2-1:-1]

print(palindrome('acd'))
print(palindrome1('abba'))
print()

print('--- Reverse integer ---', inspect.getframeinfo(inspect.currentframe()).lineno)

def rev_int(num):
    result = ''
    num_str = str(num)
    i = len(num_str)-1
    while i >= 0:
        result += num_str[i]
        i-=1
    return int(result)

def rev_int1(num):
    return "".join(list(reversed(str(num))))

print(rev_int(51))
print(rev_int(0))
print(rev_int(123))
print(rev_int1(56))

print('---Max chars/Highest Frequency---', inspect.getframeinfo(inspect.currentframe()).lineno)

def max_chars(str1):
    chars = {}
    for ch in str1:
        if ch in chars:
            chars[ch] += 1
        else:
            chars[ch] = 1
    freq = chars[ch]
    char = ''
    for ch in chars:
        if chars[ch] > freq:
            freq = chars[ch]
            char = ch
    return char

print(max_chars('abbbbccd'))
print(max_chars('44552221'))

print('--- FizzBuzz---', inspect.getframeinfo(inspect.currentframe()).lineno)

def fizz_buzz(num):
    for x in range(1,num+1):
        if x % 3 == 0 and x % 5 == 0:
            print('fizzbuzz')
        elif x % 3 == 0:
            print('fizz')
        elif x % 5 == 0:
            print('buzz')
        else:
            print(x)

print(fizz_buzz(15))

print('--- array chunking---', inspect.getframeinfo(inspect.currentframe()).lineno)

# given array and chunk size, divide the array into many subarrays
# where each subarray is of length size
# append remaining elements to a new list
def arr_chunk(arr, size):
    out = []
    chunk = []
    s = size
    for x in arr:
        if s == 0:
            out.append(chunk)
            chunk = []
            s = size
        chunk.append(x)
        s-=1
    out.append(chunk)
    return out

print(arr_chunk([1,2,3,4],2))

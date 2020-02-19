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
    for i in range(len(str1)-1,-1,-1):
        result += str1[i]
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
print()

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
print()

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
print()

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
print()

print('--- Bubble Sort ---', inspect.getframeinfo(inspect.currentframe()).lineno)

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for k in range(0, n-i-1):
            if arr[k] > arr[k+1]:
                arr[k+1], arr[k] = arr[k], arr[k+1]
    return arr

def bubble_sort1(arr):
    n = len(arr)
    for i in range(n):
        for k in range(0, n-i-1):
            if arr[k] > arr[k+1]:
                arr[k+1], arr[k] = arr[k], arr[k+1]
    return arr

# my solution
def bubble_sort2(arr):
    for _ in range(len(arr)):
        for k in range(len(arr)-1):
            if arr[k] > arr[k+1]:
                arr[k+1], arr[k] = arr[k], arr[k+1]
    return arr

print(bubble_sort([1,5,3,8,2,3]))
print(bubble_sort1([1,5,3,8,2,3]))
print(bubble_sort2([1,5,3,8,2,3,9,4]))

print('--- Anagrams ---', inspect.getframeinfo(inspect.currentframe()).lineno)

def anagram(str1,str2):
    str1 = str1.strip(' ')
    str2 = str2.strip(' ')
    freq1 = {}
    freq2 = {}
    if len(str1) != len(str2):
        return False
    for i,j in zip(str1,str2):
        if i in freq1:
            freq1[i] += 1
        else:
            freq1[i] = 1
        if j in freq2:
            freq2[j] += 1
        else:
            freq2[j] = 1
    for x in freq1:
        if x not in freq2 or freq1[x] != freq2[x]:
            return False
    return True

print(anagram('rail safety','fairy tales'))
print()
    
print('--- Capitalize Strings ---', inspect.getframeinfo(inspect.currentframe()).lineno)

def cap_str(str1):
    words = str1.split(' ')
    words = [word[0].upper()+word[1:] for word in words]
    return " ".join(words)

def cap_str1(str1):
    result = str1[0].upper()
    for x in range(1,len(str1)):
        if str1[x-1] == ' ':
            result += str1[x].upper()
        else:
            result += str1[x]
    return result

print(cap_str('a lazy fox'))
print(cap_str1('a lazy fox'))
print()

print('--- printing steps ---', inspect.getframeinfo(inspect.currentframe()).lineno)

def print_steps(num):
    l = num
    for x in range(num+1):
        print('#' * x + ' ' * l)
        l-=1

def print_steps1(num):
    for x in range(0,num):
        out = ''
        for j in range(0,num):
            if j <= x:
                out += '#'
            else:
                out += ' '
        print(out)

print(print_steps(4))
print_steps1(4)
print()

print('--- zeros at back ---')
# given an array of numbers and zeros, move all the zeros to the back of the array 
# and all the numbers before the zeros
# try to do in O(n) time

def zeros_to_back(L):
    back = []
    result = []
    for x in L:
        if x == 0:
           back.append(x)
        else:
            result.append(x)
    result.extend(back)
    return result

print(zeros_to_back([1,0,4,1,0,3,0,5]))
print()
print('--- first non repeating char ---')
# given a string return the first non repeating char in the string

def non_repeating(S):
    repeat = {}
    for char in S:
        if char in repeat:
            repeat[char] += 1
        else:
            repeat[char] = 1

    for i in repeat:
        if repeat[i] == 1:
            return i
print(non_repeating('srtirninsgtgd'))
print()

print('--- balance brackets ---')
# given a string of closing parentheses check whether it is balanced
# 3 types or parenthesis (), [], and {}
# asssume no other characters nor spaces
# example-> balanced = '([])' , not balanced = '([)]'
def balance(S):
    if len(S) % 2 != 0:
        return False

    open_b = set('([{')
    pairs = set([('(',')'), ('[',']'), ('{','}')])

    stack = []
    
    for x in S:
        if x in open_b:
            stack.append(x)
        else:
            if len(stack) == 0:
                return False
            opening = stack.pop()
            if (opening,x) not in pairs:
                return False
    return len(stack) == 0

print(balance('[(())}]'))
print(balance(''))
print()

print('--- binary search ---')
# given a list of sorted numbers and a target value create a function that uses 
# binary search to search if a value is in the list

def binary_search(L, target):
    if len(L) == 0:
        return False
    else:
        mid = len(L)//2
        
        if target == L[mid]:
            return True
        elif target < L[mid]:
            left = L[:mid]
            return binary_search(left, target)
        elif target > L[mid]:
            right = L[mid+1:]
            return binary_search(right, target)

print(binary_search([1,2,3,4,5], 4))
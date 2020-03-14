def balance(s):
    if len(s) % 2 != 0:
        return False
    
    stack = []
    opens = set('({[')
    matches = set([('(',')'),('{','}'),('[',']')])

    for x in s:
        if x in opens:
            stack.append(x)
        else:
            if len(stack) == 0:
                return False
            
            last = stack.pop()

            if (last,x) not in matches:
                return False
    return len(stack) == 0

print(balance('({[]})'))

def permutation(s):
    out = []

    if len(s) == 1:
        out = [s]
    else:
        for i, letter in enumerate(s):
            for perm in permutation(s[:i] + s[i+1:]):
                out += [letter+perm]
    return out

def nth_fib(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return nth_fib(n-1) + nth_fib(n-2)

def coin_change(target, coins):
    min_coins = 0
    if target in coins:
        return 1
    else:
        for i in [c for c in coins if c <= target]:
            num_coins = 1 + coin_change(target-i, coins)

            if num_coins < min_coins:
                min_coins = num_coins
    return min_coins

def palindrome(s):
    rev_str = ''
    index = len(s)-1
    while index >= 0:
        rev_str += s[index]
        index -= 1
    
    if rev_str == s:
        return True

    return False

print(palindrome('abcba'))

def anagram(str1,str2):
    str1 = sorted(str1)
    str2 = sorted(str2)

    return str1 == str2

print(anagram('tom','mot'))

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for k in range(0,n-i-1):
            if arr[k] > arr[k+1]:
                arr[k+1], arr[k] = arr[k], arr[k+1]
    return arr

print(bubble_sort([8,6,4,9,12,32,4,6,7,23]))

def fizzbuzz(n):
    for i in range(1,n+1):
        if i % 3 == 0 and i % 5 == 0:
            print('FizzBuzz')
        elif i % 3 == 0:
            print('Fizz')
        elif i % 5 == 0:
            print('Buzz')
        else:
            print(i)

fizzbuzz(15)

def sum_pairs(lst, s):
    visited = set()
    for x in lst:
        diff = s - x
        if diff in visited:
            return [diff,x]
        visited.add(x)
    return []
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

print(balance('(({))'))

def coin_change(target, coins):
    min_coins = target
    if target in coins:
        return 1
    else:
        for i in [c for c in coins if c <= target]:
            num_coins = 1 + coin_change(target-i,coins)
            if num_coins < min_coins:
                min_coins = num_coins
    return min_coins

def palindrome(s):
    index = len(s)-1
    rev_str = ''
    while index >= 0:
        rev_str += s[index]
        index -= 1
    
    if rev_str == s:
        return True
    else:
        return False

print(palindrome('tacocat'))

def permute(s):
    out = []
    if len(s) == 1:
        out = [s]
    else:
        for i, letter in enumerate(s):
            for perm in permute(s[:i] + s[i+1:]):
                out += [letter+perm]
    return out

# return values that add up to target sum
def target_sum(arr, s):
    visited = set()
    for i in arr:
        diff = s - i
        if diff in visited:
            return [diff,i]
        visited.add(i)
    return []

print(target_sum([1,4,3,9,2,5],11))

# return the indices of the values that add up to the target sum
def two_sum(arr,s):
    visited = set()
    for i in arr:
        diff = s - i
        if diff in visited:
            return [arr.index(diff),arr.index(i)]
        visited.add(i)
    return []

print(two_sum([1,4,3,9,2,5],11))

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for k in range(0,n-i-1):
            if arr[k] > arr[k+1]:
                arr[k+1],arr[k] = arr[k], arr[k+1]
    return arr

print(bubble_sort([4,2,8,5,1,1,12,7]))

def anagram(s1,s2):
    return sorted(s1) == sorted(s2)

def fib(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)

def dec_to_bin(n):
    if n > 0:
        dec_to_bin(n//2)
        print(n%2, end='')

def gcd(x,y):
    while(y):
        x, y = y, x % y
    return x

l = [1,2,3,4]
p = ''.join(str(i) for i in l)
print(p)

k = '123456'
s = ''.join(i for i in k if int(i) % 2 == 0)
print(s)

def anagram2(s1,s2):
    str1 = dict()
    str2 = dict()

    for ch in s1:
        if ch in str1:
            str1[ch] += 1
        else:
            str1[ch] = 1

    for ch in s2:
        if ch in str2:
            str2[ch] += 1
        else:
            str2[ch] = 1

    for ch in str1:
        if ch not in str2:
            return False
        elif str1[ch] != str2[ch]:
            return False
    return True

print(anagram2('yoman','nmoya'))

def anagram3(s1,s2):
    for ch in s1:
        if ch not in s2 or s1.count(ch) != s2.count(ch):
            return False
    return True

print(anagram3('p',''))
# n factorial
def factorial(n):
    # base case
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

print('factorial--> ', factorial(5))

# problem 1
# return sum from 0 to the inputted integer
# ex. n=4, return 4+3+2+1+0, which = 10
def rec_sum(n):
    if n == 0:
        return 0
    else:
        return n + rec_sum(n-1)

print('recursive sum --> ', rec_sum(4))

# problem 2
# given an integer, create  function which returns the sum
# of all the individual digits in that integer
# Ex. n=4321, return 4+3+2+1
def sum_func(n):
    if n % 10 == 0:
        return 0
    else:
        return n % 10 + sum_func(n // 10)

print('sum_func --> ', sum_func(3))

# create a function that takes in a string phrase and a set of list of words
# the func will determine if it is possible to split the string in  a way in which
# words can be made from the list of words.
def word_split(phrase, word_list, output=None):
    if output is None:
        output = []
    
    for word in word_list:
        if phrase.startswith(word):
            output.append(word)
            return word_split(phrase[len(word):], word_list, output)
    return output

print('word_split --> ', word_split('themanran', ['the','ran','man']))

# Interview problem 1
# Reverse a string using recursion
# slicing or iteration wont work
def reverse(s):
    if len(s) <= 1:
        return s
    else:
        return reverse(s[1:]) + s[0]
        #return s[len(s)-1] + reverse(s[:-1])

print('reverse string recursion --> ', reverse('string'))

# interview problem 2
# string permutation
# given a string write a function that uses recursion to output
# a list of all the possible permutations of that string
# Ex. s='abc', return ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']
def permute(s):
    out = []

    # base case
    if len(s) == 1:
        out = [s]
    else:
        # for every letter in string
        for i, letter in enumerate(s):
            # for every permutation
            for perm in permute(s[:i] + s[i+1:]):
                # add to output
                out += [letter+perm]
    return out

print('permute string --> ', permute('abc'))

# interview problem 3
# fibonacci sequence
# implement fibonacci sequence 3 ways:
# recursive, dynamically and iteratively
# accept a number n and return the nth number of the fibonacci sequence
def fib_rec(n):
    if n == 0 or n == 1:
        return n
    else:
        return fib_rec(n-1) + fib_rec(n-2)

print('fib rec --> ', fib_rec(10))

#fib using dynamic programming
# cache
n = 10
cache = [None] * (n+1)
def fib_dyn(n):
    # base case
    if n == 0 or n == 1:
        return n
    #check cache
    if cache[n] != None:
        return cache[n]
    # set cache
    cache[n] = fib_dyn(n-1) + fib_dyn(n-2)

    return cache[n]

print('fib dyn --> ', fib_dyn(10))
print('fib cache --> ', cache)
# fib using iteration
def fib_iter(n):
    a,b = 0,1

    for _ in range(n):

        a,b = b, a+b

    return a

print('fib iter --> ', fib_iter(10))

#interview problem 4
# coin change problem
# recursion
# given a target amount n and a list (array) of distinct coin values
# whats the fewest coins needed to make the change amount
def coin_change(target, coins):
    min_coins = target
    if target in coins:
        return 1
    else:
        # for every coin value that is <= my target value
        for i in [c for c in coins if c <= target]:

            num_coins = 1 + coin_change(target-i,coins)

            if num_coins < min_coins:
                min_coins = num_coins

    return min_coins

#coin change problem using dynamic programming
def coin_change_dyn(target, coins, known_results):
    min_coins = target

    if target in coins:
        known_results[target] = 1
        return 1
    # return known result if > 1
    elif known_results[target] > 0:
        return known_results[target]
    else:
        # for every coin value <= target
        for i in [c for c in coins if c <= target]:
            num_coins = 1 + coin_change_dyn(target-i, coins, known_results)

            if num_coins < min_coins:
                min_coins = num_coins

            # reset known result
            known_results[target] = min_coins
    return min_coins

print('dyn coin change --> ', coin_change_dyn(74, [1,5,10,25], [0]*(74+1) ))

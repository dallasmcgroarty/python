# balance parenthesis/bracket/sqaure
# coin change problem
# recursion
# string manipulation
# all permutations of given string

# function that takes in a string of words and returns the words
# in the string but if a word length is even, split the word in half
# and return the two

#100x100 grid bingo, how to check if a bingo was scored

def balance(s):
    if len(s) % 2 != 0:
        return False

    stack = []
    opens = set('({[')
    matches = set([('(',')'),('[',']'),('{','}')])

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

print(balance('({()})'))

def permute(s):
    out = []

    if len(s) == 1:
        out = [s]
    else:
        for i, letter in enumerate(s):
            for perm in permute(s[:i] + s[i+1:]):
                out += [letter+perm]
    return out

print(permute('abc'))

def split_words(s):
    out = []
    words = s.split(' ')
    for word in words:
        if len(word) % 2 == 0:
            mid = len(word) // 2
            out.append(word[:mid])
            out.append(word[mid:])
        else:
            out.append(word)
    return out

print(split_words('hello there my name is uncle tom'))

# coin change problem
# recursion
# given a target amount n and a list (array) of distinct coin values
# whats the fewest coins needed to make the change amount
def coin_change(target, coins):
    min_coins = target
    if target in coins:
        return 1
    else:
        for i in [c for c in coins if c < target]:
            num_coins = 1 + coin_change(target-i, coins)

            if num_coins < min_coins:
                min_coins = num_coins
    return min_coins

print(coin_change(40,[1,2,3,4]))

        
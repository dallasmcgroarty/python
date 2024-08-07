import sys
import statistics

def reverse(str):
    reversed = ''
    for i in range(len(str),0, -1): # or use reversed function i.e. for i in reversed(str):
        reversed += str[i-1]
    return reversed
print('reversed string', reverse('string'))
def temperature(temp):
    if temp <= 30:
        return 'colder'
    elif temp <= 50:
        print('cold')
    elif temp <= 70:
        print('warm')
    elif temp <= 100:
        print('hot')

print('temp--> ', temperature(30))

string1 = '1,2,3,4,5,6,7'

string1 = string1.replace(',','')

print('no commas --> ', string1)
print(type(string1))

sum1 = 0
for i in string1:
    sum1 += int(i)

print(sum1)

str1 = "hello"
str2 = reverse(str1)
print(str2)

def merge_list(list1, list2):
    sorted_list = []
    left = 0
    right = 0

    while(left < len(list1) and right < len(list2)):
        if list1[left] <= list2[right]:
            sorted_list.append(list1[left])
            left += 1
        else:
            sorted_list.append(list2[right])
            right += 1
    if left == len(list1):
        while right < len(list2):
            sorted_list.append(list2[right])
            right += 1
    else:
        while left < len(list1):
            sorted_list.append(list1[left])
            left += 1
    return sorted_list

list1 = [2,5,8,9,10,12]
list2 = [1,2,5,6,7,11,14]

new_list = merge_list(list1,list2)

print('merged lists --> ', new_list)

# merge list practice again
def merge_list2(l1,l2):
    left = right = 0
    result = []

    while left < len(l1) and right < len(l2):
        if l1[left] <= l2[right]:
            result.append(l1[left])
            left += 1
        else:
            result.append(l2[right])
            right += 1
    if left == len(l1):
        while right < len(l2):
            result.append(l2[right])
            right += 1
    else:
        result.append(l1[left])
        left += 1
    return result

# return first missing positive integer in a list/array
def firstMissingPositive(A):
        A.sort()
        n = 1
        for x in A:
            if x > 0:
                if x != n:
                    return n
                else:
                    n+=1
        return n

print('first missing positive integer --> ', firstMissingPositive([1,2,3,4,5,7,8,9]))

# return duplicate in list/array in O(N) time
def repeatedNumber(A):
         out = set()
         for x in A:
             if x in out:
                 return x
             out.add(x)
         print(out)
         return -1
        # or do it this way
        # for x in A:
        #     if(A.count(x) > 1):
        #         return x

print('first duplicate in a list --> ', repeatedNumber([1,3,4,5,8,10,24,12,5]))

def max_value(num):
    max = num[0]
    for x in num:
        if x > max:
            max = x
    return max

print('max value in list --> ', max_value([4,7,9,3,40,23,1,5]))

# given a non negative list of numbers, add 1 to the number and return it as a list
# ex input [1,2,3,4] ex  [2,3,9]
# output [1,2,3,5]   ex  [2,4,0]
def plusOne(A):
    num_str = ''.join(str(val) for val in A)
    add_one = int(num_str) + 1
    add_one = str(add_one)
    # ret_list = []
    # for char in add_one:
    #     ret_list.append(int(char))
    # #return list(add_one)
    # return ret_list
    return [int(char) for char in add_one]
print('add one to list of numbers --> ', plusOne([1,3,4,5,9]))

# return input list as a wave like list, where a1 >= a2 <= a3 >= a4 <= a5
def wave(A):
    n = 0
    A.sort()
    while n < len(A) - 1:
        A[n], A[n+1] = A[n+1], A[n]
        n+=2
    return A

print('list as wave --> ', wave([4,3,8,9,7]))

str1 = 'python'
ret_string = ''
index = len(str1)
while index > 0:
    ret_string += str1[index - 1]
    index = index - 1
print(ret_string)

# return max sum contiguous subarray
def maxSubArray(A):
    current_max = A[0]
    final_max = A[0]
    for i in range(1,len(A)):
        current_max = max(A[i], current_max + A[i])
        final_max = max(current_max, final_max)
    return final_max

arr1 = [-120, -202, -293, -60, -261, -67, 10, 82, -334, -393, -428, -182, -138, -167, -465, -347, -39, -51, -61, -491, -216, -36, -281, -361, -271, -368, -122, -114, -53, -488, -327, -182, -221, -381, -431, -161, -59, -494, -406, -298, -268, -425, -88, -320, -371, -5, 36, 89, -194, -140, -278, -65, -38, -144, -407, -235, -426, -219, 62, -299, 1, -454, -247, -146, 24, 2, -59, -389, -77, -19, -311, 18, -442, -186, -334, 41, -84, 21, -100, 65, -491, 94, -346, -412, -371, 89, -56, -365, -249, -454, -226, -473, 91, -412, -30, -248, -36, -95, -395, -74, -432, 47, -259, -474, -409, -429, -215, -102, -63, 80, 65, 63, -452, -462, -449, 87, -319, -156, -82, 30, -102, 68, -472, -463, -212, -267]
print('max sum contiguous subarray --> ', maxSubArray(arr1))

# max set
def maxset(A):
    sets = {}
    curr_set = []
    count = 0
    for x in A:
        curr_set.append(x)
        if(x < 0):
            curr_set.pop()
            sets['set'+str(count)] = curr_set.copy()
            count+=1
            curr_set.clear()
        if(x == A[len(A)-1]):
            sets['set'+str(count)] = curr_set.copy()

    max_sum = 0
    curr_max = 0

    for numbers in sets.values():
        curr_max = sum(numbers)
        if(curr_max > max_sum):
            max_sum = curr_max
    
    for key, value in sets.items():
        if(max_sum == sum(value)):
            return sets[key]


print('max set --> ', maxset([1,4,5,-4,2,4,-3,1,3]))

#return intersection of two lists, return type is a list
listex = ['a','b','z']
listp = ['x','y','z']
def intersection(a,b):
    set1 = set(a)
    set2 = set(b)
    set3 = set1 & set2
    return list(set3)

# or do 
def intersection2(a,b):
    return [val for val in set(a) & set(b)]
print('intersection of two lists --> ', intersection2(listex, listp))

# given a string return a dict with key as letter and value as count
# of that letter in the string 
def multiple_letter_count(word):
    return {key: word.count(key) for key in word}
print('multiple letter count --> ', multiple_letter_count('awesome'))

#check if palindrome
def is_palindrome(word):
    word.replace(' ', '')
    rev_str = ''
    for x in range(len(word), 0, -1):
        rev_str += word[x - 1]
    if(rev_str == word):
        return True
    return False

#check if palindrome
def is_palindrome1(word):
    strip = word.replace(' ', '')
    return strip == strip[::-1]
print('palindrome --> ', is_palindrome1('tacocat'))

# capitalize first letter in string
def capitalize(string):
    return string[:1].upper() + string[1:]
    # or
    # return word.replace(word[0], word[0].upper())

# given list and a func, return a list of true and false values in
# another list
def partition(A, func=None):
    truthy = []
    falsy = []
    for x in A:
        if(func(x)):
            truthy.append(x)
        else:
            falsy.append(x)
    return [truthy, falsy]
    
'''
given a 6x6 matrix of integers
and hourglass is defined as 
a b c 
  d
e f g
calculate the total of every value in each hourglass in the matrix
return the max hourglass sum
'''
def hourglassSum(arr):
    max_result = -sys.maxsize - 1
    total = 0

    for i in range(0, 4):
        for j in range(0, 4):
            total = arr[i][j] + arr[i][j+1] + arr[i][j+2] + arr[i+1][j+1] + arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2]
            if(total > max_result):
                max_result = total
    return max_result

# min swaps in an unordered consecutive array
# when ordered => 1,2,3,4,5 each numbers is 
# its own index if index starts at 1 not 0
def minimumSwaps(arr):
    numSwaps = 0
    i = 0
    while(i < len(arr)-1):
        if arr[i] != i+1:
            tmp = arr[i]
            arr[i], arr[tmp-1] = arr[tmp-1], arr[i]
            numSwaps += 1
        else:
            i += 1
    return numSwaps

print(minimumSwaps([2,3,4,1,5]))

# given an array a and number d, rotate the array to the left d times
# input: a = [1,2,3,4,5] d = 3
# return: a = [4,5,1,2,3] 
def rotLeft(a, d):
    for _ in range (0,d): # using _ because we dont keep track of/store the iteration
        popped = a.pop(0)
        a.append(popped)
    return a

print('rotate array left ==> ', rotLeft([1,2,3,4,5], 3))

A = [1,1,1,1,1,1,2,2,2,2,2]

def solution(A):
    n = len(A)
    L = [-1] + A
    count = 0
    pos = (n + 2) // 2
    candidate = L[pos]
    for i in range(1, n + 1):
        if (L[i] == candidate):
            count = count + 1
        if (count >= pos):
            return candidate
    return -1
print('Element in more than half of array ==> ', solution(A))

# return number of unique pairs
# given a list of numbers
ar = [10, 20, 20, 10, 10, 30, 50, 10, 20]

def numPairs(ar):
    pairs = 0
    seen = set()
    for i in range(0, len(ar)):
        if ar[i] in seen:
            continue
        numCopies = ar.count(ar[i])
        seen.add(ar[i])
        if numCopies % 2 == 0 and numCopies >= 2:
            pairs += numCopies // 2
        elif numCopies % 2 == 1 and numCopies > 2:
            pairs += (numCopies - 1) // 2
    print (seen)
    return pairs
print('number of unique pairs ==> ', numPairs(ar))

# given a number of steps n and string of U's(up) and D's(down)
# return the number of valleys the path has
# valley is defined as going down from sea-level and back up to sea-level
# input: 4, DUDU
# visual: \/\/
# output: 2
#
def countingValleys(n, s):
    down = 0
    up = 0
    valleys = 0
    for step in range(0 , n):
        if s[step] == 'U' and up == down - 1:
            valleys += 1
            up = 0
            down = 0
        elif s[step] == 'D':
            down += 1
        elif s[step] == 'U':
            up += 1
    return valleys

# return number of alternating characters/ deletions
def alternatingCharacters(s):
    count = 0
    for i in range(0, len(s) - 1):
        if s[i] == s[i+1]:
            count += 1
    return count

# function that returns true or false based off if the string is valid
# all char in string must have the same frequency, if one char frequency
# is off by 1 then you can remove it and the string is valid
# but, you can only remove 1 character at 1 index
def isValid(s):
    repeat = set()
    # freq = {char: s.count(char) for char in s}
    common = s.count(s[0])
    count = 0
    for x in range(0, len(s)):
        test = s.count(s[x])
        if s[x] in repeat:
            continue
        else:
            if test > common or test < common:
                count += 1
            repeat.add(s[x])
    if count > 1:
        return 'NO'
    else:
        return 'YES'

# give a length of array n, and a list of queries with 3 elements a,b,k
# where a = start, b = end, k = sumand
# add each summand to elements between a and b for all queries
# then return the max sum in the array
def arrayManipulation(n, queries):
    # found solution
    A = [0] * (n + 1)
    max_sum = 0
    count = 0
    for first, last, value in queries:
        A[first-1] += value
        A[last] -= value
    
    for x in A:
        count += x
        if count > max_sum:
            max_sum = count
    return max_sum

    # my original solution
    
    # manipArray = [0] * n
    # max_sum = 0
    # for x in range(len(queries)):
    #     for p in range(queries[x][0]-1, queries[x][1]):
    #         manipArray[p] += queries[x][2]
    #         if(manipArray[p] > max_sum):
    #             max_sum = manipArray[p]
    # return max_sum

# not working correct cuz indexing list of lists 
print('array manip function -> ', arrayManipulation(5,[[1,2,100]]))

# return maximum number of toys that can be bought given a list of prices
# and a max amount to spend
def maximumToys(prices, k):
    max_toys = 0
    prices.sort()
    for x in prices:
        if x < k:
            max_toys += 1
            k -= x
    return max_toys

print('Max num toys ==> ', maximumToys([14,2,15,18,25,36,4,6,21], 100))

# given list of expenditures and number or days
# notifications will sent if number of days is up
# and the current expenditure is greater of equal to
# the median of the trailing days * 2 
# return num of notifications left

# apparently not fast enough for large inputs
def activityNotifications(expenditure, d):
    #prev = expenditure[0:d]
    notifs = 0
    for i in range(d, len(expenditure)):
        median = statistics.median(expenditure[i-d:i])
        if expenditure[i] >= 2 * median:
            notifs += 1
    return notifs

strrr = "hdlgg"
print(list(strrr))
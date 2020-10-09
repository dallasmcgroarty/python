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
print(palindrome1('aca'))
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

print(arr_chunk([1,2,3,4],3))
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

def anagram1(str1,str2):
    return sorted(str1) == sorted(str2)

print(anagram1('yoop','poy'))

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

print('--- zeros at back ---', inspect.getframeinfo(inspect.currentframe()).lineno)
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
print('--- first non repeating char ---', inspect.getframeinfo(inspect.currentframe()).lineno)
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

print('--- balance brackets ---', inspect.getframeinfo(inspect.currentframe()).lineno)
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

print('--- binary search ---', inspect.getframeinfo(inspect.currentframe()).lineno)
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
print()

print('--- equal sides of array ---', inspect.getframeinfo(inspect.currentframe()).lineno)
# You are going to be given an array of integers. Your job is to take that array
# and find an index N where the sum of the integers to the left of N is equal to 
# the sum of the integers to the right of N. If there is no index that would make 
# this happen, return -1.
def equal_sides(arr):
    for i in range(0,len(arr)):
        left = sum(arr[:i])
        right = sum(arr[i+1:])
        if left == right:
            return i
    return -1

print(equal_sides([2,3,4]))
print()

print('--- Alphabet Position ---', inspect.getframeinfo(inspect.currentframe()).lineno)
# given a string of text, return a string where each char in the text 
# is replaced with its position in the alphabet
def alphabet_position(text):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    return ' '.join([str(alphabet.index(char.lower())+1) for char in text if char.lower() in alphabet])

print(alphabet_position("The sunset sets at twelve o' clock."))
print()

print('--- Duplicates and Non-Dupes ---', inspect.getframeinfo(inspect.currentframe()).lineno)
# return a new string where each character in the new string is '(' 
# if that character appears only once in the original word, or ')' 
# if that character appears more than once in the original word. 
# Ignores capitalization when determining if a character is a duplicate.
def duplicate_encode(word):
    freq = {}
    ret_str = ''
    for x in word:
        if x == ' ':
            continue
        elif x.lower() in freq:
            freq[x.lower()] += 1
        else:
            freq[x.lower()] = 1
    
    for x in word:
        if x == ' ':
            ret_str += ' '
        elif freq[x.lower()] > 1:
            ret_str += ')'
        else:
            ret_str += '('
    return ret_str

    #could also use count() which gets the count of that item in the string/array/dict
    # for char in word:
    #     if word.count(char) > 1:
    #         ret_str += ')'
    #     else:
    #         ret_str += '('
    # return ret_str
print(duplicate_encode('hello there'))
print()

print('--- Hours, Minutes, Seconds ---', inspect.getframeinfo(inspect.currentframe()).lineno)
# create a functions that takes in a number of seconds and returns it in human readable
# format that looks like HH:MM:SS, where HH <= 99, MM <= 59, SS <= 59
def humanTime(s):
     return '{:02}:{:02}:{:02}'.format(s // 3600, s // 60 % 60, s % 60)

    # or do :
    # h= seconds/60**2
    # m= (seconds%60**2)/60
    # s= (seconds%60**2%60)
    # return "%02d:%02d:%02d" % (h, m, s)
print(humanTime(43000))
print()

print('--- Sort the odd ---', inspect.getframeinfo(inspect.currentframe()).lineno)
# create a function that takes in an array and returns a sorted array
# but only the odds are sorted and evens remain in their place
# ex) input = [2,9,11,6,8,7], output = [2,7,9,6,8,11]
def sort_array_odds(source_array):
    odds = []
    for i in range(0,len(source_array)):
        if source_array[i] % 2 == 1:
            odds.append(source_array[i])
    odds.sort()
    index = 0
    for i in range(0,len(source_array)):
        if source_array[i] % 2 == 1:
            source_array[i] = odds[index]
            index += 1
    return source_array

print(sort_array_odds([2,9,11,6,8,7]))
print()

print('--- Write Number in Expanded Form ---', inspect.getframeinfo(inspect.currentframe()).lineno)
# create a function that takes a number and write it out in an expanded
# form like:
# 12 = '10 + 2', 100 = '100', 70304 = '70000 + 300 + 4'
def expanded_form(num):
    expanded = ''
    num = str(num)[::-1]
    count = 0
    while count < len(num):
        if count == 0 and num[count] is not '0':
            expanded = num[count]
        if count >= 1 and num[count] is not '0':
            expanded = num[count] + '0'*count + ' ' + expanded 
        count += 1
    result = expanded.split()
    result = ' + '.join(num for num in result)
    return result

print(expanded_form(30643))
print()

print('--- A chain adding function ---', inspect.getframeinfo(inspect.currentframe()).lineno)
# create function that adds numbers together when called in succession
# add(1)(2) -> returns 3
# add(1)(2)(3)(4) -> returns 10
# add(1) -> return 1
# can also save to variable and call:
# addTwo = add(2)
# addTwo + 5 -> 7
# addTwo(3) -> 5
class add(int):
    def __call__(self, value):
        return add(self+value)

print('--- Split Strings ---', inspect.getframeinfo(inspect.currentframe()).lineno)
#Complete the solution so that it splits the string into pairs of two characters. 
# If the string contains an odd number of characters then it should replace the missing 
# second character of the final pair with an underscore ('_').
def split_strings(s):
    pairs = []
    if len(s) % 2 != 0:
        s+= '_'
    for i in range(0, len(s), 2):
        pairs.append(s[i:i+2])
    return pairs

print(split_strings('adfffggrhra'))

print('--- Fibonacci ---', inspect.getframeinfo(inspect.currentframe()).lineno)
# given the nth fib number, print that fibonacci number
def nth_fib(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return nth_fib(n-1) + nth_fib(n-2)

print('--- Exchange List elements ---', inspect.getframeinfo(inspect.currentframe()).lineno)
def exchange_with(a, b):
    temp = []
    temp1 = []
    index = len(a)-1
    while index >= 0:
        temp.append(a[index])
    
    index = len(b)-1
    while index >= 0:
        temp1.append(b[index])
    
    for i in range(0, len(temp1)):
        a[i] = temp1[i]
    
    for i in range(0, len(temp)):
        b[i] = temp[i]

a = [1,2,3]
b = ['a','b','c']
#exchange_with(a,b)
print(a,b)

print('--- Persistence num ---', inspect.getframeinfo(inspect.currentframe()).lineno)
# given a number, multiple each digit together until the product is a single digit
# if product is not a single digit, multiply that product together, and so on
# return the number of times needed to reach a single digit
# ex: input = 39 , 3*9 = 27, 2*7 = 14, 1*4 = 4, return 3
# because we needed to multiple the digits out 3 times until we reached a single digit
def persistence(n):
    # recursive solution
    count = 0
    if n <= 9:
        return count
    else:
        nums = str(n)
        product = int(nums[0])
        for i in range(1,len(nums)):
            product *= int(nums[i])
        return 1 + persistence(product)

print(persistence(39))

print('--- Sum pairs/ Two Sum ---', inspect.getframeinfo(inspect.currentframe()).lineno)
# sum of pairs, aka two sum, return values that add to the target sum
def sum_pairs(ints, s):
    already_visited = set()
    for i in ints:
        difference = s - i
        if difference in already_visited:
            return [difference, i]
        already_visited.add(i)
    return []

# two sum, return indices that the value and those indices equals the target sum
def sum_pairs1(ints, s):
    already_visited = set()
    for i in ints:
        difference = s - i
        if difference in already_visited:
            return [ints.index(difference), ints.index(i)]
        already_visited.add(i)
    return []

print(sum_pairs1([1,3,2,8,4], 7))

print('--- convert decimal to binary ---',inspect.getframeinfo(inspect.currentframe()).lineno)
# decimal to binary
def dec_to_bin(n):
    if n > 0:
        dec_to_bin(n//2)
        print(n%2, end="")

dec_to_bin(17)
print()

print('--- GCD/HCF ---', inspect.getframeinfo(inspect.currentframe()).lineno)
#GCD or HCF (highest common factor/greatest common denominator)
# using euclidean algo
def gcd(x,y):
    while(y):
        x, y = y, x % y
    return x

# recursive approach
def gcd1(a,b):
    if (b==0):
        return a
    else:
        return gcd1(b, a%b)

print(gcd(60,48))

print('--- Moving totals ---', inspect.getframeinfo(inspect.currentframe()).lineno)
# moving totals
# function should determine if a sum of 3 consecutive numbers
# is in the list of numbers
def movingTotals(numbers,total):
    result = set()
    for i in range(len(numbers)):
        result.add(sum(numbers[i:i+3]))
    if total in result:
        return True
    else:
        return False

print(movingTotals([1,3,4,5,4,8,7,3,4,2,1],7))

print('--- Human readable ---', inspect.getframeinfo(inspect.currentframe()).lineno)
# create a functions that takes in a number of seconds and returns it in human readable
# format that looks like HH:MM:SS, where HH <= 99, MM <= 59, SS <= 59
def make_readable(seconds):
    hours = seconds//3600
    minutes = (seconds%3600)//60
    sec = seconds%60
    return "{:02}:{:02}:{:02}".format(hours,minutes,sec)

print(make_readable(26492))

print('--- max sum contiguos subarray ---', inspect.getframeinfo(inspect.currentframe()).lineno)
# if array is empty or all elements are negatie return 0
# return the max sum contigous subarray
def maxSequence(arr):
    if not arr:
        return 0
    
    negatives = 0
    if arr[0] < 0:
        negatives += 1
        
    current_max = arr[0]
    final_max = arr[0]
    
    for i in range(1,len(arr)):
        if arr[i] < 0:
            negatives += 1
        current_max = max(arr[i], current_max + arr[i])
        final_max = max(current_max, final_max)
    if negatives == len(arr):
        return 0
    return final_max

print(maxSequence([1,5,3,-1,2,4,-2,4]))
print()
print('--- move zeros to back ---', inspect.getframeinfo(inspect.currentframe()).lineno)
# move all zeros in the list to the back while keeping the order of the 
# non-zeros the same
# the list also has strings and boolens to handle, specifically false
def zeros_back(arr):
    back = []
    result = []
    for num in arr:
        if type(num) == bool or num != 0:
            result.append(num)
        else:
            back.append(0)
    result.extend(back)
    return result

print('--- no sign multiply ---', inspect.getframeinfo(inspect.currentframe()).lineno)
# multiply two integers without using the multiplication or divison sign
def no_sign_multiply(a,b):
    result = 0
    for _ in range(0,b):
        result += a
    return result

print(no_sign_multiply(4,3))

print('--- get remainder ---', inspect.getframeinfo(inspect.currentframe()).lineno)
# get remainder of two numbers without using divison or modulo
def remainder(a,b):
    while a - b > 0:
        a = a - b
    return a
print(remainder(10,4))
print()

print('--- palindrome given int ---', inspect.getframeinfo(inspect.currentframe()).lineno)
# palindrome checker given integer
def pal(x):
    num = []
    num = str(x)
    index = len(num)-1
    reverse = ''
    while index >= 0:
        reverse += num[index]
        index -= 1
    return num == reverse
print(pal(1221))
print()
print('--- roman numeral to integer ---', inspect.getframeinfo(inspect.currentframe()).lineno)
# roman numeral to integer
def romanToInt(s):
    result = 0
    romans = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100,'D':500,'M':1000, 
            'IV':4, 'IX':9, 'XL':40, 'XC':90, 'CD':400, 'CM':900}
    i = 0
    group = ''
    while i < len(s):
        if i != len(s)-1:
            group = s[i] + s[i+1]
        if group in romans:
            result += romans[group]
            group = ''
            i += 2
        else:
            result += romans[s[i]]
            i += 1
    return result

print(romanToInt('MCXCV'))
print()

print('--- longest common prefix ---', inspect.getframeinfo(inspect.currentframe()).lineno)
# longest common prefix
# find longest common prefix amongst an array of strings
# if none in common return ""
def longestCommonPrefix(strs):
    common = ''
    if len(strs) == 0:
        return ''
    for i in range(len(strs[0])):
        for j in range(1,len(strs)):
            if i == len(strs[j]):
                return common
            if strs[0][i] != strs[j][i]:
                return common
        common += strs[0][i]
    return common

print(longestCommonPrefix(['flower','flowing','flowy','flowski']))
print()

print('--- merge sorted list and return a listnode ---', inspect.getframeinfo(inspect.currentframe()).lineno)
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def addNode(val, L):
    temp = L
    while temp.next:
        temp = temp.next
    temp.next = ListNode(val)

# merge two sorted lists and return a sorted list in form
# of a listnode
def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
    flag = 1
    sorted_list = ListNode()
    while l1 != None and l2 != None:
        if l1.val <= l2.val:
            if flag == 0:
                sorted_list = ListNode(l1.val)
                flag = 1
                l1 = l1.next
            else:
                addNode(l1.val, sorted_list)
                l1 = l1.next
        else:
            if flag == 0:
                sorted_list = ListNode(l2.val)
                flag = 1
                l2 = l2.next
            else:
                addNode(l2.val, sorted_list)
                l2 = l2.next
    if l1 == None:
        while l2 != None:
            addNode(l2.val, sorted_list)
            l2 = l2.next
    else:
        while l1 != None:
            addNode(l1.val, sorted_list)
            l1 = l1.next
    return sorted_list.next

print()

print('--- remove duplicates ---', inspect.getframeinfo(inspect.currentframe()).lineno)
# remove duplicates from sorted array
# do it in-place 
def removeDuplicates(nums):
    if len(nums) == 0:
        return 0
    
    prev = nums[0]
    i = 1
    while i < len(nums):
        if prev == nums[i]:
            nums.pop(i)
        else:
            prev = nums[i]
            i += 1
print()

print('--- remove elements ---', inspect.getframeinfo(inspect.currentframe()).lineno)
# remove all values in list equal to the value passed in to function
def removeElement(nums, val):
    i = 0
    while i < len(nums):
        if nums[i] == val:
            nums.pop(i)
        else:
            i += 1

print()

print('--- substring function ---', inspect.getframeinfo(inspect.currentframe()).lineno)
# implement substring function
# given a string and a substring, return the index of the first occurrence
# of the substring in the string, if the sub string exists
def strStr(haystack, needle):
    if len(needle) == 0:
        return 0
    length = len(needle)
    i = 0
    while i < len(haystack):
        if haystack[i:i+length] == needle:
            return i
        i += 1
    return -1

print('--- search or insert function ---', inspect.getframeinfo(inspect.currentframe()).lineno)
# Given a sorted array and a target value, return the index if the target 
# is found. If not, return the index where it would be if it were inserted in order.
# no duplicates in array
def searchInsert(nums, target):
    insert = 0
    i = 0
    while i < len(nums):
        if target > nums[len(nums)-1]:
            return len(nums)
        if nums[i] == target:
            return i
        else:
            if nums[i] < target and nums[i+1] > target:
                insert = i + 1
        i += 1
    return insert

print()

print('--- plus one to list num ---', inspect.getframeinfo(inspect.currentframe()).lineno)
# function takes in a list of numbers representing an integer
# return the number + 1 as a list
def plusOne(digits):
    number = ''.join([str(digit) for digit in digits])
    number = int(number) + 1
    return [int(num) for num in str(number)]

print()

print('--- remove dupes in list ---', inspect.getframeinfo(inspect.currentframe()).lineno)
# remove duplicates in sorted list
def deleteDuplicates(head):
    temp = head
    while temp and temp.next:
        if temp.val == temp.next.val:
            temp.next = temp.next.next
        else:
            temp = temp.next
    return head
print()

print('--- max sum subarray ---', inspect.getframeinfo(inspect.currentframe()).lineno)
# find the contiguous subarray which has the largest sum
# and return its sum
def maxSubArray(self, nums):
    if not nums:
        return 0

    current_max = nums[0]
    final_max = nums[0]
    
    for i in range(1, len(nums)):
        current_max = max(nums[i], current_max + nums[i])
        final_max = max(current_max, final_max)
    return final_max
print()

print('--- length of last word in string ---', inspect.getframeinfo(inspect.currentframe()).lineno)
# Given a string s consists of upper/lower-case alphabets 
# and empty space characters ' ', return the length of last word 
# (last word means the last appearing word if we loop 
# from left to right) in the string.
# If the last word does not exist, return 0.
def lengthOfLastWord(self, s):
    words = s.strip(' ').split(' ')
    print(words)
    if not words:
        return 0
    return len(words[-1])
print()

print('--- merge sorted arrays again ---', inspect.getframeinfo(inspect.currentframe()).lineno)
# Given two sorted integer arrays nums1 and nums2, 
# merge nums2 into nums1 as one sorted array.

# The number of elements initialized in nums1 and nums2 are m and n respectively
def merge(self, nums1, m, nums2, n):
    """
    Do not return anything, modify nums1 in-place instead.
    """
    if not nums2:
        return nums1
    
    left = 0
    right = 0
    
    while len(nums1) > m:
        nums1.pop()
        
    while left < len(nums1) and right < len(nums2):
        if nums2[right] < nums1[left]:
            nums1.insert(left, nums2[right])
            right += 1
        left += 1

    if left >= m:
        while right < len(nums2):
            nums1.insert(left, nums2[right])
            left += 1
            right += 1
print()

print('--- majority element ---', inspect.getframeinfo(inspect.currentframe()).lineno)
# return most frequent element that appears in the majority
# of the list
def majorityElement(self, nums):
    result = dict()
    for i in nums:
        if i in result:
            result[i] += 1
        else:
            result[i] = 1
    for num in result:
        if result[num] > len(nums) // 2:
            return num

def sumofpairs(nums, s):
    seen = set()
    for i in nums:
        diff = s - i
        if diff in seen:
            return [diff, i]
        seen.add(i)
    return []

print(sumofpairs([1,4,3,2,5,6], 7))
print()

print('--- sorted array to BST ---', inspect.getframeinfo(inspect.currentframe()).lineno)
# given array where elements are sorted in ascending order, conver it to 
# a height balanced BST
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def sortedArrayToBST(nums):
    def buildBST(left, right):
        if left > right:
            return None
        
        mid = (left + right) // 2
        
        newNode = TreeNode(nums[mid])
        newNode.left = buildBST(left, mid-1)
        newNode.right = buildBST(mid+1, right)
        return newNode
    return buildBST(0, len(nums)-1)

print()

print('--- Check for cycle in linked list ---', inspect.getframeinfo(inspect.currentframe()).lineno)
# determing if there is a cycle in the linked list
# linked list node is:
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
def hasCycle(self, head):
    seen = set()
    temp = head
    while temp:
        if temp in seen:
            return True
        seen.add(temp)
        temp = temp.next
    return False
    
print()

print('--- list of dicts to list of names ---', inspect.getframeinfo(inspect.currentframe()).lineno)
# list of dicts to list of names
segments = [{'name': 'Wallstreet', 'average_spend': 82.01}, {'name': 'Gambler', 'average_spend': 107.00}, {'name': 'Parents', 'average_spend': 10.52}]
names = [x['name'] for x in segments]
print(names)

names = []
for item in segments:
    names.append(item['name'])
#print(names)

names = list(map(lambda item: item['name'], segments))
#print(names)
print()

print('--- buy/sell stocks to max profit ---', inspect.getframeinfo(inspect.currentframe()).lineno)
# buy and sell stocks to maximize profit
def buy_sell(prices):
    if len(prices) == 1:
        return 0
    cur_profit = 0
    max_profit = 0
    start = 0
    end = 1
    while start < len(prices) - 1 and end < len(prices):
        if prices[end] > prices[start]:
            if cur_profit < prices[end] - prices[start]:
                cur_profit = prices[end] - prices[start]
            end += 1
        elif prices[end] < prices[start]:
            max_profit += cur_profit
            cur_profit = 0
            start = end
            end = start + 1
        if end == len(prices):
            max_profit += cur_profit
    return max_profit

print(buy_sell([100,180,260,310,40,535,695]))
print()

print('--- two sum, return index ---', inspect.getframeinfo(inspect.currentframe()).lineno)
# given array of numbers in sorted ascending order, and target number
# return index of first two elements that sum to the target
# return as list
def twoSum(numbers, target):
    #visited = set()
    #for num in numbers:
        #if target - num in visited:
        #    if numbers.index(target-num)+1 == numbers.index(num)+1:
        #         return [numbers.index(target-num)+1, numbers.index(num)+2]
        #      return [numbers.index(target-num)+1, numbers.index(num)+1]
        #   visited.add(num)
    #return []
    left = 0
    right = len(numbers) - 1
    while left < right:
        total = numbers[left] + numbers[right]
        if total > target:
            right -= 1
        elif total < target:
            left += 1
        else:
            return [left+1,right+1]
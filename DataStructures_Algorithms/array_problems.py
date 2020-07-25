# return string true if s2 is anagram of s1 else false
def anagram(s1,s2):
    #strip white spaces and make lowercase
    s1 = s1.replace(' ','').lower()
    s2 = s2.replace(' ','').lower()
    
    # sort both strings and compare
    return sorted(s1) == sorted(s2)

print('anagram => ', anagram('dog','god')) #true
print('anagram => ', anagram('abc','cba')) #true
print('anagram => ', anagram('aabbcc','aabbc')) #false
print('anagram => ', anagram('123',' 1 2')) #false

# anagram with clearer code
def anagram2(s1,s2):
    s1 = s1.replace(' ','').lower()
    s2 = s2.replace(' ','').lower()

    #edge case
    if len(s1) != len(s2):
        return False
    
    count = {}

    for letter in s1:
        if letter in count:
            count[letter] += 1
        else:
            count[letter] = 1
    
    for letter in s2:
        if letter in count:
            count[letter] -= 1
        else:
            count[letter] = 1
    
    for k in count:
        if count[k] != 0:
            return False
    
    return True

print('anagram2 => ', anagram2('abc','cba')) #true
print('anagram2 => ', anagram2('clint eastwood','old west action')) # true
print('anagram2 => ', anagram2('abcd','cba'))

# given array and a sum, return the number of pairs that sum to k
def pair_sum(arr,k):
    if len(arr) < 2:
        return
    
    #using sets to track seen
    seen = set()
    output = set()

    for num in arr:
        target = k - num

        if target not in seen:
            seen.add(num)
        
        else:
            output.add( (min(num, target), max(num, target)) )
    return len(output)

print('pair sum => ', pair_sum([1,3,2,2],4)) # 2
print('pair sum => ', pair_sum([1,2,3,1],3)) # 1
print('pair sum => ', pair_sum([1,9,2,8,3,7,4,6,5,5,13,14,11,13,-1],10)) # 6

# given array of nonnegative integers. A second array is given with the elements of
# the first arry shuffled around and a random element is missing
# find the missing element
# runs in O(n) time - linear
def missing_element(A,B):
    count = {}
    for x in B:
        if x in count:
            count[x] += 1
        else:
            count[x] = 1
    for x in A:
        if count[x] == 0:
            return x
        else:
            count[x] -= 1

print('missing element => ', missing_element([5,5,7,7],[5,7,7]))

#given an array of integers(positive or negative) find the largest continuous sum
def largest_cont_sum(A):

    if len(A) == 0:
        return 0

    cur_sum = max_sum = A[0]

    for x in A[1:]:
        cur_sum = max(cur_sum + x, x)

        max_sum = max(cur_sum, max_sum)

    return max_sum

print('Largest continuous Sum => ', largest_cont_sum([1,2,-1,3,4,10,10,-10,-1]))

#reverse a string
def rev_str(s):
    # strip whitespace
    s = s.strip()
    new_str = ''
    i = len(s)-1
    while(i >= 0):
        new_str += s[i]
        i -= 1
    return new_str

print('reversed string => ', rev_str('geeks'))

#reverse a sentence
# 'This is the best' => 'best the is This'
def rev_sentence(s):
    words = []
    cur_str = ''
    ret_str = ''
    # filter the words out
    for x in s:
        if x == ' ' and not cur_str:
            pass
        elif x == ' ' and cur_str:
            words.insert(0,cur_str)
            cur_str = ''
        elif x == s[len(s)-1] and cur_str:
            cur_str += x
            words.insert(0,cur_str)
        else:
            cur_str += x
    
    # convert words to strings and add to final string
    # add space after each
    for x in words:
        ret_str += str(x)
        if x != words[len(words)-1]:
            ret_str += ' '
    return ret_str

#faster/cleaner solution is to do:
# return ' '.join(reversed(s.split()))

print('sentence reversal => ', rev_sentence('This is the best'))
print('sentence reversal => ', rev_sentence('Hi John,    are you ready to go?'))

# string compression, input 'AAABBCCCC' becomes 'A3B2C4'. 
# case sensitive

def compress(s):
    letters = {}
    compressed = ''
    for x in s:
        if x in letters:
            letters[x] += 1
        else:
            letters[x] = 1
    
    for key, value in letters.items():
        compressed += key + str(value)

    return compressed

print('string compression => ', compress('AAABBCCCC')) # A3B2C4
print('string compression => ', compress('AAAaaaCCBB')) # A3a3C2B2

# given a string return true if all characters are unique or false if not

def unique(s):
    if len(s) == 0:
        return True

    chars = set()
    for x in s:
        if x in chars:
            return False
        else:
            chars.add(x)
    return True

print('Unique characters => ', unique('')) #true
print('Unique characters => ', unique('goo')) #false
print('Unique characters => ', unique('abcdefg')) #true

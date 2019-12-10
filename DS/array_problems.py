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
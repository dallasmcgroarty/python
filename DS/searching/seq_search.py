# basic searching algorithm of sequentially checking
# every element in a list
# O(n) worst case

def seq_search(arr, target):
    for x in arr:
        if x == target:
            return True
    return False

arr = [1,2,3,4,5]
print(seq_search(arr, 2))


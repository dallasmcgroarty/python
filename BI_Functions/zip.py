# zip function
# makes an iterable that takes elements from each of the iterables
# takes elements from each iterable at the same positon and creates a pair,triplet,etc

nums1 = [1,2,3,4,5]
nums2 = [6,7,8,9,10]
z = zip(nums1,nums2)
z1 = zip(nums1,nums2)
p = zip(nums1,nums2)
# use list or dict to convert zip object
print(list(z))
print(dict(z1))

words = ['hi','lol','haha','smiley']
z2 = zip(words, nums1,nums2)
print(list(z2))

# use zip and * in front of the iterable to unpack it and get the orignal iterables
print(list(zip(*p)))

#*********
# more complex zip usage
print("more complex zipping---")

midterms = [80,91,78]
finals = [98,89,53]
students = ['dan','ang','kate']

#final grades = {'dan': 98,'ang':91,'kate':78}

# create a dict with each students name and their highest grade using zip 
final_grades = {t[0]:max(t[1],t[2]) for t in zip(students,midterms,finals)}
print(final_grades)

# same thing but using map and lambda
final_scores = dict(
    zip(
        students,
        map(
            lambda pair: max(pair),
            zip(midterms,finals)
        )
    )
)
print(final_scores)

# same thing but getting the average score
final_avg_grades = {t[0]:(t[1] + t[2])/2 for t in zip(students,midterms,finals)}
print(final_avg_grades)
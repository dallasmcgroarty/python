#list basics, methods
my_list = [1,2,3,4] # list to use

#len() returns length of list
len(my_list)
print(len(my_list))

#append - add item to end of list
my_list.append(5)
print(my_list)

#extend - add to the end of a list a list of values
my_list.extend([6,7,8])
print(my_list)

#insert - insert an item at a given position
my_list.insert(1, "Hello") #puts Hello in index 1 and pushes everything after 1 index up
print(my_list)

#clear - removes all items from the list (not used that often)
my_list2 = [1,2,3,4]
my_list2.clear()

#pop - remove item at given position in the list and return it (takes index)
# if no index is specified, removes & returns last item in the list
popped_item = my_list.pop(1)
print(popped_item)
my_list.pop()
print(my_list)

#remove - removes the *first* item from the list whose value is x (takes value not index)
# throws error if not found
my_list.remove(3)
print(my_list)

#index - returns the index of item in list, can also take a start and end argument
position = my_list.index(4)
print(position)
position = my_list.index(5,2)
print(position)

#count - returns the number of times x appears in the list
my_list.extend([7,7])
print(my_list)
num = my_list.count(7)
print(num)

#reverse - reverses elements of the list (in-place)
my_list.reverse()
print(my_list)

#sort - sort the items of the list (in-place), can take arguments to specify sorting
my_list.sort()
print(my_list)

#join - join elements in a list and convert to string
#if elements are strings
words = ["Coding", "is", "cool"]
str_words = ' '.join(words)
print(str_words)

#if elements are numbers, need to convert to string
nums = [1,2,3,4]
str_nums = ', '.join(str(val) for val in nums)
print(str_nums)

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
# cursors keep your place in the file
# after a read the cursor is at the end of the file
# seek() method used to move the cursor

file = open('FileIO/story.txt')
print(file.read())
file.seek(0)
print(file.read())
file.seek(20)
print(file.read())
file.seek(0)
print()
# readline() used to read a single line in a file

print(file.readline())
file.seek(0)

lines = file.readlines()

for line in lines:
    print(line)

# use close() to close a file after reading or writing
file.close()
print('--using with keyword')
# with keyword for opening a file
# with opens the file, can read or write and then closes the file after the loop
with open('FileIO/story.txt') as file:
    data = file.read()

print(data)
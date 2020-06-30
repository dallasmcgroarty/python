# can also use open() to write to a file
# use 'w' flag to open for writing
# using 'w' overwrites the exisiting contents
# use 'a' to append to the end of the file
with open('FileIO/story.txt', 'a') as file:
    file.write('Writing to the file\n')
    file.write('Using forward slash n to add a new line \n')

with open('FileIO/story.txt') as file:
    print(file.read())


# can write to a non existing file to create a new file
with open('FileIO/newFile.txt','w') as file:
    file.write('This is a new file')

with open('FileIO/newFile.txt') as file:
    print(file.read())
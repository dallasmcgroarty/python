# modes for opening files
# - r -read a file
# - w - write to a file (previous contents removed)
# - a - append to a file (appends to end of existing file)
# - r+ - read and write to a file(writing based on cursor)

def statistics(fileN):
    with open(fileN) as file:
        lines = file.readlines()
 
    return { "lines": len(lines),
             "words": sum(len(line.split(" ")) for line in lines),
             "characters": sum(len(line) for line in lines) }
        
print(statistics('FileIO/story.txt'))

# create a function that accepts a file and returns a dictionary where
# {lines: number of lines, words: number of words, characters: number of characters}
# in the file
def statistics(fileN):
    with open(fileN) as file:
        lines = file.readlines()
 
    return { "lines": len(lines),
             "words": sum(len(line.split(" ")) for line in lines),
             "characters": sum(len(line) for line in lines) }
        
print(statistics('FileIO/story.txt'))

# create a function that takes in a file, a word in the file, and a word to replace that word
# replace all occurences of the old word with the new word in the file
def find_and_replace(file_name, old_word, new_word):
    with open(file_name, "r+") as file:
        text = file.read()
        new_text = text.replace(old_word, new_word)
        file.seek(0)
        file.write(new_text)
        file.truncate()
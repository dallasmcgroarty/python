# reading csv files
# csv files are common for tabular data
# python has a built in csv module to read csvs

# reading csv regularly
with open('CSV/fighters.csv', 'r') as f:
    print(f.read())


# CVS Module
# reader() lets you iterate over rows of the CSV as lists
# DictReader() lets you iterate over rows of the CSV as OrderedDicts

from csv import reader
# reader saves each row in the csv as a list but in an iterator
# reader reaches end of file after use
with open('CSV/fighters.csv') as f:
    csv_reader = reader(f)
    # using next to skip first row
    next(csv_reader)
    for row in csv_reader:
        print(f"{row[0]} is from {row[1]}")
        #print(row)
print()

# convert the csv to a list of lists
with open('CSV/fighters.csv') as f:
    csv_reader = reader(f)
    data = list(csv_reader)
    print(data)
print()

# using DictReader
from csv import DictReader
with open('CSV/fighters.csv') as f:
    csv_reader = DictReader(f)
    for row in csv_reader:
        print(row['Name'])

# create a function that takes in a first and last name and checks if they are in the csv file or not
# return the index if found otherwise return not found
def find_user(first, last):
    with open('users.csv') as f:
        csv_reader = reader(f)
        index = 0
        for row in csv_reader:
            if row[0] == first and row[1] == last:
                return index
            index+=1
        return first + ' ' + last + ' not found.'
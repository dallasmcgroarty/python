from csv import reader,writer

# two different method to write:

# with open('CSV/fighters.csv') as f:
#     csv_reader = reader(f)
#     fighters = [[s.upper() for s in row] for row in csv_reader]

# with open('CSV/screaming_fighters.py', 'w') as f:
#     csv_writer = writer(f)
#     for fighter in fighters:
#         csv_writer.writerow(fighter)

with open('CSV/fighters.csv') as f:
    csv_reader = reader(f)
    with open('CSV/screaming_fighters.py', 'w') as f:
        csv_writer = writer(f)
        for fighter in csv_reader:
            csv_writer.writerow([s.upper() for s in fighter])
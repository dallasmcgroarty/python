# writing to csv files
# can use lists of dicts to write to csv
# writer - creates a write object for writing to csv
# writerow - method on writer to write a row to the CSV

from csv import writer, DictWriter, DictReader
# with open('CSV/cats.csv', 'w') as f:
#     csv_writer = writer(f)
#     csv_writer.writerow(["Name", "Age"])
#     csv_writer.writerow(["Blue","3"])
#     csv_writer.writerow(["Sam", "4"])

# writing to CSV files using dictionaries
with open('CSV/cats.csv', 'w') as f:
    headers = ["Name", "Breed", "Age"]
    csv_writer = DictWriter(f, fieldnames=headers)
    csv_writer.writeheader()
    csv_writer.writerow({
        "Name": "Garfield",
        "Breed": "Tabby",
        "Age": 10
    })

# using dictwriter and dictreader
# convert cm in csv to inches
def cm_to_in(cm):
    return float(cm) * 0.393701

with open('CSV/fighters.csv') as f:
    csv_reader = DictReader(f)
    fighters = list(csv_reader)

with open('CSV/inches_fighters.csv', 'w') as f:
    headers = ["Name", "Country", "Height"]
    csv_writer = DictWriter(f, fieldnames=headers)
    csv_writer.writeheader()
    for fighter in fighters:
        csv_writer.writerow({
            "Name": fighter["Name"],
            "Country":fighter["Country"],
            "Height": cm_to_in(fighter["Height (in cm)"])
        })
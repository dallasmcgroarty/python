# python dictionaries
# key,value pairs

test_dict = {'a': 2, 'b': 3, 'c': 4}
print(test_dict)
print(test_dict['a'])

# add to dictionary by adding unused key, otherwise it will overwrite existing key
test_dict['d'] = 5
print(test_dict)

# empty dict
empty_dict = {}

#loop dict
for key in test_dict:
  print(f'{key}: {test_dict[key]}')

# loop key, val pairs with .items()
for key, val in test_dict.items():
  print(f'{key}: {val}')


student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}

student_grades = {}

for key in student_scores:
  if student_scores[key] >= 91:
    student_grades[key] = 'Outstanding'
  elif student_scores[key] >= 81 and student_scores[key] <= 90:
    student_grades[key] = 'Exceeds Expectations'
  elif student_scores[key] >= 71 and student_scores[key] <= 80:
    student_grades[key] = 'Acceptable'
  elif student_scores[key] <= 70:
    student_grades[key] = 'Fail'

print(student_grades)

# nesting lists and dicts
travel_log = {
  'France': ['Paris','Lille','Dijon'],
  'Germany': ['Berlin','Hamburg']
}

travel_log_2 = {
  'France': {'cities_visited': ['Paris','Lille','Dijon'], 'total_visits': 12},
  'Germany': ['Berlin','Hamburg']
}

travel_log_3 = [
  {'country': 'France', 'cities_visited': ['Paris','Lille','Dijon'], 'total_visits': 12},
  {'country': 'Germany', 'cities_visited': ['Berlin', 'Hamburg'], 'total_visits': 5}
]

# working with dicts
country = 'Brazil'
visits = 5
list_of_cities = ["Sao Paulo", "Rio de Janeiro"]

travel_log = [
  {
    "country": "France",
    "visits": 12,
    "cities": ["Paris", "Lille", "Dijon"]
  },
  {
    "country": "Germany",
    "visits": 5,
    "cities": ["Berlin", "Hamburg", "Stuttgart"]
  },
]

def add_new_country(country, visits, list_of_cities):
  entry = {}
  entry['country'] = country
  entry['visits'] = visits
  entry['cities'] = list_of_cities
  travel_log.append(entry)

add_new_country(country, visits, list_of_cities)

print(f"I've been to {travel_log[2]['country']} {travel_log[2]['visits']} times.")
print(f"My favourite city was {travel_log[2]['cities'][0]}.")
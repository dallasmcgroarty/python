import re

def parse_name(s):
    name_regex = re.compile(r'^(Mr.|Mrs.|Ms.|Mdme.) (?P<first>[A-Za-z]+) (?P<last>[A-Za-z]+)$')
    match = name_regex.search(s)
    if match:
        print(match.groups())
        print(match.group('first'))
        print(match.group('last'))

parse_name('Mrs. Tilda Swinton')
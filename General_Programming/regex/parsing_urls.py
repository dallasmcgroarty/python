import re

# can use () around some regex to get multiple matches
# then use .groups() which returns a tuple of all matches
url_regex = re.compile(r'(https?)://(www.[A-za-z-]{2,256}.[a-z]{2,6})([-a-zA-Z0-9@:%_/+.~#?&//=]*)')
match = url_regex.search('http://www.youtube.com/videos/dd&')
print(match.groups())
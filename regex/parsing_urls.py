import re

url_regex = re.compile(r'(https?)://(www.[A-za-z-]{2,256}.[a-z]{2,6})([-a-zA-Z0-9@:%_/+.~#?&//=]*)')
match = url_regex.search('http://www.youtube.com/videos/dd&')
print(match.groups())
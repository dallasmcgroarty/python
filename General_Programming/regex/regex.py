import re

# r in front of string for raw string
# allows you to not have to escape characters like \
pattern = re.compile(r'\d{3} \d{3}-\d{4}')

# search only gets first match
res = pattern.search('Call me at 415 555-4242 or 310 334-8921')

r1 = pattern.findall('Call me at 415 555-4242 or 310 334-8921')

print(res)
print(res.group())
print(r1)
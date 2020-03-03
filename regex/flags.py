import re

pat = re.compile(r'^([a-z0-9_.-]+)@([0-9a-z.-]+).([a-z.]{2,6})$')

# can use verbose to comment out regex to make it clearer
pattern = re.compile(r"""
    ^([a-z0-9_.-]+)  # first portion of email
    @                # single @ sign
    ([0-9a-z.-]+)    # email provider
    \.                # single period
    ([a-z.]{2,6})$   # com, org, net, etc...
""", re.VERBOSE)

match = pattern.search("thomas123@yahoo.com")
print(match.group())
print(match.groups())
# regular expressions are a way of descrbing patterns within 
# search strings
# potential use cases:
    # - validating emails/passwords
    # - validating credit card number
    # - validating phone numbers
    # - advanced find/replace text
    # - formatting text/output
    # - syntax highlighting

"""
Some Regex syntax:
    \d - digit 0 - 9
    \w - letter, digit, or underscore
    \s - whitespace character
    \D - not a digit
    \W - not a word character ie (*]%$ etc...
    \S - not a whitespace character
    . - and character except line break

Some Regex Quantifiers:
    + - one or more
    {x} - exactly x times. {3} = 3 times
    {x,y} - x to y times. {3, 5} = 3 to 5 times
    {x,} - x or more times. {4,} = 4 or more times
    * - zero or more times
    ? - once or none
"""
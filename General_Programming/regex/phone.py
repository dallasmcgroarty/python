import re

def extract_phone(s):
    phone_regex = re.compile(r'\b\d{3} \d{3}-\d{4}\b')
    match = phone_regex.search(s)
    if match:
        return match.group()
    return None

def extract_all_phones(s):
    phone_regex = re.compile(r'\b\d{3} \d{3}-\d{4}\b')
    match = phone_regex.findall(s)
    if match:
        return match
    return None

def is_valid_phone(s):
    phone_regex = re.compile(r'^\d{3} \d{3}-\d{4}$')
    match = phone_regex.search(s)
    if match:
        return True
    return False

# can also use fullmatch function to find exact match
def is_valid_phone1(s):
    phone_regex = re.compile(r'\d{3} \d{3}-\d{4}')
    match = phone_regex.fullmatch(s)
    if match:
        return True
    return False

print(extract_phone('here is a number 714 744-4445'))
print(extract_phone('here is a number 714 744-4445444'))
print(extract_phone('714 744-4332 hee haw'))
print(extract_phone('714 744-4332'))
print(extract_all_phones('call me at 714 444-3235 or at 715 445-3332'))

print(is_valid_phone('714 744-4332'))
print(is_valid_phone('714 744-4332 asdd'))
print(is_valid_phone('dda 714 744-4332 d'))
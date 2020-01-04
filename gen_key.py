import hashlib
s_key = 'dkey4h561k'

user = input('Enter username: ')
user = user.strip()

to_hash = user + s_key

m = hashlib.md5(to_hash.encode('utf-8'))
hash = m.hexdigest()
print(hash[0:6])
import hashlib
s_key = 'dkey4h561k'

addr = input('Enter MAC address: ')
addr = addr.strip()

to_hash = addr + s_key

m = hashlib.md5(to_hash.encode('utf-8'))
hash = m.hexdigest()
print(hash[0:6])
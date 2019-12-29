import hashlib
m = hashlib.md5('dallasdkey4h561k'.encode('utf-8'))
hash = m.hexdigest()
print(hash[0:6])
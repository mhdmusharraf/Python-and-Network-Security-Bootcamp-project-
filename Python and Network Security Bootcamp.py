

x = input()

import hashlib
#1st question
hash_object = hashlib.md5(x.encode()) # encode() :Converts the string into bytes to be acceptable by hash function
hash_dig = hash_object.hexdigest()    # hexdigest() : Returns the encoded data in hexadecimal format
print(hash_dig)
#2nd question
hash_object = hashlib.sha224(x.encode())
hex_dig = hash_object.hexdigest()
print(hex_dig)

hash_object = hashlib.sha256(x.encode())
hex_dig = hash_object.hexdigest()
print(hex_dig)

hash_object = hashlib.sha384(x.encode())
hash_dig = hash_object.hexdigest()
print(hash_dig)


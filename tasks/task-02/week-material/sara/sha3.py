import sys
import hashlib
if sys.version_info < (3, 6):
    import sha3
# sha3_224 algorithm from the hashlib module.
s = hashlib.sha3_224()
# will output the name of the hashing algorithm currently in use.
print(s.name)
# Get the input from the user
data = input("Please Enter the data to hash: ").encode('utf-8')
# providing the input to the hashing algorithm.
s.update(data)
print(s.hexdigest())
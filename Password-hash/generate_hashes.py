import hashlib

password = "python_is_fun"
# Find the Hash of password
hash = hashlib.sha256(password.encode('utf-8'))
# Print hashed password Object
print(f'hash: {hash}')
# Print hashed password - the hash
print(f'hash.hexdigest(): {hash.hexdigest()}')


import hashlib

pass_found = 0

i_hash = input('Enter the hashed password: ')

# C:\Users\IGS\Desktop\Web\vscode\Unethical-Hacking-Tools\Password-hash\ai-recognition\my_common_passwords.txt
#p_doc = input('\nEnter password filename full path\n[C:\file\path\list.txt]: ')
p_doc = './my_common_passwords.txt'

p_file = open(p_doc, 'r')

for word in p_file:
    enc_word = word.encode('utf-8')
    # To keep md5 hashed enc_word in hashed format using .strip()
    #hash_word = hashlib.md5(enc_word.strip())
    
    # To keep sha512 hashed enc_word in hased format using .strip()
    hash_word = hashlib.sha512(enc_word.strip())
    # Generate hexDigest of hashed password
    # returning the string representation of the hash
    digest = hash_word.hexdigest()
    
    if digest == i_hash:
        print(f'Password found: {word}')
        pass_found = 1
        break

if not pass_found:
    print(f'Password NOT found :(')
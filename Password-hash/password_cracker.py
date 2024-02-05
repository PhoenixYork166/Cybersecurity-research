import hashlib

# Preparing to store read passwors from a list.txt
common_passwords = []

# Preparing to store usernames & hashes using a Dict
user_hash_dict = {}

# Read all common passwords in a list
with open('common_passwords.txt', 'r') as f:
    common_passwords = f.read().splitlines()
    # Read common_passworsds in [] => Split lines
    #common_passwords.append(f.read().splitlines())
    # print(f'common_passwords: {common_passwords}')
    # print('\n')
    # print('=====================================')

# To separate the usernames & hashes 
# and store each line as an item in a List
with open('username_hashes.txt', 'r') as f:
    text = f.read().splitlines()
    
    # To split usernames using ":"
    # [0] = before ":"
    # [1] = after ":"
    for user_hash in text:
        username = user_hash.split(":")[0]
#         print('-----------START - Printing username ----------')
#         print(f'username: {username}')
#         print('-----------END - Printing username ----------')
#         print('\n')
        hash = user_hash.split(":")[1]
#         print('-----------START - Printing hash ----------')
#         print(f'hash: {hash}')
#         print('-----------END - Printing hash ----------')
#         print('\n')
        user_hash_dict[username] = hash
#         print(f'user_hash_dict[username]: {user_hash_dict[username]}')

# Returning Key & Value for variables in user_hash_dict        
for user, hash in user_hash_dict.items():
#     print('=========== Printing user, hash ============')
#     print('\n')
#     print(f'user, hash: \n')
    print(user, hash)
    
# Loop through each password in each line of common_passwords
for password in common_passwords:
    # Hash each password in common_passwords
    hashed_password = hashlib.sha256(password.encode('utf-8')).hexdigest()
    
    # Loop through each username, each hash in user_hash_dict{}
    for username, hash in user_hash_dict.items():
        # If 'hashed password' in username_hashes.txt matches
        # 'hash' in common_passwords.txt
        if hashed_password == hash:
            # If Hash is found
            # print {username}:{password} found
            print(f'Hash FOUND!\n{username}:{password}')
        
    #print(text)
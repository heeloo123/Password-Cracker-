import hashlib

user_hash_dictionary = {}
common_passwords =[]
with open('common-password.txt', 'r') as file:
    #common_passwords = file.read(.splitlines())
    common_passwords = (file.read().splitlines())
#print(common_passwords)

with open('user_password_hash', 'r') as file:
    text = file.read().splitlines()
    for user_hash in text:
        username = user_hash.split(":")[0]
        #print(username)
        hash = user_hash.split(":")[1]
        user_hash_dictionary[username] = hash

#for user,hash in user_hash_dictionary.items():
   # print(user,hash)

for password in common_passwords:
    hashed_password = hashlib.sha256(password.encode('utf-8')).hexdigest()
    for username, hash in user_hash_dictionary.items():
        if hashed_password == hash:
            print(f'Hash Found {username}:{password}')

import hashlib

password = 'jane1234'
hash = hashlib.sha256(password.encode('utf-8')) #The utf-8 parameter specifies the specific encoding to use when converting the string to bytes.
print(hash.hexdigest())

#The use of UTF-8 encoding ensures that any characters in the password string can be properly represented as bytes and processed by the hash function.
# UTF-8 (Unicode Transformation Format 8-bit)
#UTF-8 represents each code point as a sequence of 1 to 4 bytes (groups of 8 bits).
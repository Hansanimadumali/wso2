import hashlib
import sys
import os

if(len(sys.argv)<2):
    print("Need an password to digest")
    sys.exit()

password = sys.argv[1]
salt_value = os.urandom(16)
iterations = 200000


dk = hashlib.pbkdf2_hmac('sha512', str.encode(password), salt_value, iterations)
print(dk.hex())

import hashlib
import sys
import os

if(len(sys.argv)<2):
    print("Need an password to digest")
    sys.exit()

password = sys.argv[1]
salt_value = os.urandom(16)


dk = hashlib.sha512(str.encode(password) + salt_value)

print(dk.hexdigest())

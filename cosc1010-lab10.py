# Colton Riley
# UWYO COSC 1010
# 11/20/2024
# Lab XX
# Lab Section: 15
# Sources, people worked with, help given to: Collin Peters helped me because i was not reading hash path file.
#   Used https://www.geeksforgeeks.org/python-hash-method/ to understand the hash() method better

#import modules you will need 

from hashlib import sha256 
from pathlib import Path

def get_hash(to_hash):
    """You can use """
    return sha256(to_hash.encode('utf-8')).hexdigest().upper()

rockyoupath = Path('rockyou.txt')
hashcontent = Path('hash')

rockyoucontent = rockyoupath.read_text()
rockyoulist = rockyoucontent.split('\n')

hash_string = hashcontent.read_text()

for line in rockyoulist:
    linehash = get_hash(line)
    if linehash == hash_string:
        print(line)
        break
    else:
        continue





# Files and Exceptions

# For this assignment, you will be writing a program to "crack" a password. You will need to open the file `hash` as this is the password you are trying to "crack."

# To begin, you will need to open the 'rockyou.txt' file:
# - This file contains a list of compromised passwords from the rockyou dump.
# - This is an abridged version, as the full version is quite large.
# - The file contains the plaintext version of the passwords. You will need to hash them to check against the password hash you are trying to crack.
#   - You can use the provided `get_hash()` function to generate the hashes.
#   - Be careful, as "hello" and "hello " would generate a different hash.

# You will need to include a try-except-catch block in your code.
# - The reading of files needs to occur in the try blocks.


# - Read in the value stored within `hash`.
#   - You must use a try and except block.


# Read in the passwords in `rockyou.txt`.
# - Again, you need a try-except-else block.
# Hash each individual password and compare it against the stored hash.
# - When you find the match, print the plaintext version of the password.
# - End your loop.

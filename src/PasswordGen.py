#Password Generator
#Alex Graalum
#CS 362
#4-15-2021
import random
import string
characters = string.ascii_lowercase + string.ascii_uppercase + string.digits 

num = input("Enter password length: ")
print("Your password is: " + ''.join(random.choice(characters) for i in range(num)))
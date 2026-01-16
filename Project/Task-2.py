print("Password Checker")
print()

# get password
pwd = input("Enter your password: ")

# check length
if len(pwd) < 9:
    print("Password too short.")
    exit()

# good length
print("Password OK.")
print()

# random stuff
import random

# first check
n1 = random.randint(1, len(pwd))
a1 = input(f"Letter at position {n1}: ")
if a1 == pwd[n1-1]:
    print("Correct")
else:
    print()
    print("Security check failed.")
    exit()

# second check  
n2 = random.randint(1, len(pwd))
a2 = input(f"Letter at position {n2}: ")
if a2 == pwd[n2-1]:
    print("Correct")
else:
    print()
    print("Security check failed.")
    exit()

# third check
n3 = random.randint(1, len(pwd))
a3 = input(f"Letter at position {n3}: ")
if a3 == pwd[n3-1]:
    print("Correct")
else:
    print()
    print("Security check failed.")
    exit()

# all good
print()
print("Security check passed.")

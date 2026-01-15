"""
Checks that the password matches and is between 8 and 12 characters long.
"""

p1 = input("Enter a new password: ")
p2 = input("Confirm password: ")

valid = p1 == p2 and 8 <= len(p1) <= 12
print("Password set" if valid else "Error: invalid password")

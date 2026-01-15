"""
Prevents the use of common passwords.
"""

BAD_PASSWORDS = ["password", "letmein", "sesame", "hello", "justinbieber"]

p1 = input("Enter a new password: ")
p2 = input("Confirm password: ")

valid = p1 == p2 and 8 <= len(p1) <= 12 and p1 not in BAD_PASSWORDS
print("Password set" if valid else "Error: invalid password")

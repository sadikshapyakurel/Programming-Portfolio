"""
Prompts the user to enter a password twice and checks if they match.
"""

p1 = input("Enter a new password: ")
p2 = input("Confirm password: ")

print("Password set" if p1 == p2 else "Error: passwords do not match")

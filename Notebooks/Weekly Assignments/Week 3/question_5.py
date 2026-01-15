"""
Repeats password entry until a valid password is chosen.
"""

BAD_PASSWORDS = ["password", "letmein", "sesame", "hello", "justinbieber"]

while True:
    p1 = input("Enter a new password: ")
    p2 = input("Confirm password: ")

    valid = p1 == p2 and 8 <= len(p1) <= 12 and p1 not in BAD_PASSWORDS

    if valid:
        print("Password set")
        break
    print("Error: invalid password")

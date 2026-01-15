"""
Greets the user by name.
If no name is entered, it greets the user as "Stranger".
"""

name = input("What is your name? ").strip()
print(f"Hello, {'Stranger' if name == '' else name}!")

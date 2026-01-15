"""
Greets the user with the name properly capitalised.
"""

def format_name(name):
    return name.capitalize() if name else "Stranger"


print(f"Hello, {format_name(input('What is your name? ').strip())}!")

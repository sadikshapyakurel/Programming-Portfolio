"""
Removes the last character from a string if possible.
"""
def remove_last(text):
    return text[:-1] if len(text) > 1 else text

print(remove_last(input("Enter text: ")))

"""
Returns the number of uppercase and lowercase letters in a string.
"""

def count_case(text):
    return (
        sum(c.isupper() for c in text),
        sum(c.islower() for c in text)
    )
u, l = count_case(input("Enter text: "))
print("Uppercase:", u)
print("Lowercase:", l)


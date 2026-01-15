"""
Displays a times table chosen by the user between 0 and 12.
"""

table = int(input("Enter a number between 0 and 12: "))

for i in range(13):
    print(f"{i} x {table} = {i * table}")

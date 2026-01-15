"""
Prints a times table.
If the number is negative, the table is printed backwards.
"""

table = int(input("Enter a number: "))
number = abs(table)

sequence = range(12, -1, -1) if table < 0 else range(13)

for i in sequence:
    print(f"{i} x {number} = {i * number}")

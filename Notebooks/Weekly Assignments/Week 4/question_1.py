"""
Checks if a number is between 0 and 100 inclusive.
"""
def is_valid(n):
    return 0 <= n <= 100

print(is_valid(int(input("Enter a number: "))))

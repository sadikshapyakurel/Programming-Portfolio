"""
Convert a positive integer to binary (without the '0b' prefix).
"""

def to_binary(n):
    return bin(n)[2:]  

print(to_binary(10)) 

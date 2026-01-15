"""
Converts a centigrade temperature given as input like 25C to fahrenheit.
"""

def parse_celsius(value):
    return float(value[:-1])

def c_to_f(c):
    return (c * 9 / 5) + 32

temp = parse_celsius(input("Enter temperature (e.g. 25C): ").upper())
print(f"{c_to_f(temp)}F")

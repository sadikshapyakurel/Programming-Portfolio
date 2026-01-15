"""
Converts temperatures between centigrade and fahrenheit.
"""

def c_to_f(c):
    return (c * 9 / 5) + 32


def f_to_c(f):
    return (f - 32) * 5 / 9


print(c_to_f(0))
print(f_to_c(32))

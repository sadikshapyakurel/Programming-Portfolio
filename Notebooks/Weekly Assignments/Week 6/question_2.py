"""
Return factors of a number as a list.
"""

def factors(num):
    result = []
    for i in range(1, num+1):
        if num % i == 0:
            result.append(i)
    return result

print(factors(12))  

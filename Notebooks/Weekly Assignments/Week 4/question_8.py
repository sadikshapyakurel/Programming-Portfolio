"""
Reads six centigrade temperatures and displays max, min, and mean.
"""

from statistics import mean

def read_celsius():
    return float(input("Enter temperature (e.g. 20C): ").upper()[:-1])


temps = [read_celsius() for _ in range(6)]

print("Max:", max(temps))
print("Min:", min(temps))
print("Mean:", mean(temps))

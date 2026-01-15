"""
Processes any number of centigrade temperatures until Enter is pressed.
"""

from statistics import mean

def read_celsius(value):
    return float(value[:-1])


temps = []

while True:
    value = input("Enter temperature (e.g. 20C): ").upper()
    if value == "":
        break
    temps.append(read_celsius(value))

print("Max:", max(temps))
print("Min:", min(temps))
print("Mean:", mean(temps))

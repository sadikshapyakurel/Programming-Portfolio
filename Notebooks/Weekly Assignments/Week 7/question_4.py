"Write a program that counts letters in a message (case-insensitive) and prints the six most common letters and counts."
from collections import Counter

def six_common_letters(msg):
    msg = msg.lower()
    letters = [c for c in msg if c.isalpha()]
    c = Counter(letters)
    for letter, count in c.most_common(6):
        print(f"{letter}: {count}")

six_common_letters("This is an example message to analyze letter frequency.")




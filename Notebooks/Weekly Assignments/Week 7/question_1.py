"Write a function that takes a string and returns a sorted list of its unique letters. For example, 'cheese' returns ['c', 'e', 'h', 's']."
def unique_letters(s):
    return sorted(set(s))
print(unique_letters("cheese"))

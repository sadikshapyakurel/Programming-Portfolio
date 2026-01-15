"Write three functions, each taking two words, returning sorted lists of: letters in either word, letters in both, letters in only one."

def letters_in_either(w1, w2): return sorted(set(w1) | set(w2))
def letters_in_both(w1, w2): return sorted(set(w1) & set(w2))
def letters_in_one_only(w1, w2): return sorted(set(w1) ^ set(w2))

print(letters_in_either("hello", "world"))   
print(letters_in_both("hello", "world"))    
print(letters_in_one_only("hello", "world")) 

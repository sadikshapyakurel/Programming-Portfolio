"""Unix spell: print words not found in dictionary"""
import sys
import string

if len(sys.argv) != 2:
    print("Usage: python question_5.py <filename>")
    sys.exit(1)

filename = sys.argv[1]

try:
    with open('dictionary.txt', 'r', encoding='utf-8') as dfile:
        dictionary = set(word.strip().lower() for word in dfile)

    with open(filename, 'r', encoding='utf-8') as f:
        text = f.read()

    translator = str.maketrans('', '', string.punctuation)
    cleaned_text = text.translate(translator)

    words = cleaned_text.lower().split()

    unknown_words = set(word for word in words if word not in dictionary)

    if unknown_words:
        print("Words not found in dictionary:")
        for w in sorted(unknown_words):
            print(w)
    else:
        print("All words found in dictionary.")

except FileNotFoundError as e:
    print(f"File not found: {e.filename}")
except Exception as e:
    print(f"Error: {e}")


"""Unix wc: count lines and characters in a file"""

import sys

if len(sys.argv) != 2:
    print("Usage: python question_4.py <filename>")
    sys.exit(1)

filename = sys.argv[1]

try:
    with open(filename, 'r', encoding='utf-8') as f:
        text = f.read()

    lines = text.count('\n') + 1 if text else 0
    chars = len(text)

    print(f"Lines: {lines}")
    print(f"Characters: {chars}")

except FileNotFoundError:
    print(f"File '{filename}' not found.")
except Exception as e:
    print(f"Error: {e}")

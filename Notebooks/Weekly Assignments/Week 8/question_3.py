"""Unix grep: search for a pattern in a file and print matching lines"""

import sys

if len(sys.argv) != 3:
    print("Usage: python question_3.py \"<pattern>\" \"<filename>\"")
    sys.exit(1)

pattern = sys.argv[1]
filename = sys.argv[2]

try:
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            if pattern in line:
                print(line, end='')
except FileNotFoundError:
    print(f"File '{filename}' not found.")
except Exception as e:
    print(f"Error: {e}")

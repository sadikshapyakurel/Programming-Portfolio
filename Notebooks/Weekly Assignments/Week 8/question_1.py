"""Unix nl: print file lines with line numbers"""

import sys

if len(sys.argv) < 2:
    print("Usage: python question_1.py sample.txt")
else:
    with open(sys.argv[1]) as f:
        for i, line in enumerate(f, 1):
            print(i, line, end="")

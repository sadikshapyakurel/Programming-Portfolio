"""Unix diff: check if two files are same"""
import sys

if len(sys.argv) != 3:
    print("Usage: python question_2.py filename1.txt filename2.txt")
    sys.exit(1)

file1, file2 = sys.argv[1], sys.argv[2]

try:
    with open(file1, 'r', encoding='utf-8') as f1, open(file2, 'r', encoding='utf-8') as f2:
        lines1 = f1.readlines()
        lines2 = f2.readlines()
except FileNotFoundError as e:
    print(f"File not found: {e}")
    sys.exit(1)

max_len = max(len(lines1), len(lines2))
differences = 0

for i in range(max_len):
    line1 = lines1[i].rstrip('\n') if i < len(lines1) else ''
    line2 = lines2[i].rstrip('\n') if i < len(lines2) else ''

    if line1 != line2:
        differences += 1
        print(f"Difference at line {i+1}:")
        print(f"  File1: {line1}")
        print(f"  File2: {line2}")

if differences == 0:
    print("Files are the same.")
else:
    print(f"\nTotal differences: {differences}")

"""
Print the shortest command-line argument. If multiple shortest, print any one.
"""

import sys

def main():
    args = sys.argv[1:]
    if not args:
        print("No arguments provided.")
        return
    shortest = min(args, key=len)
    print(f"Shortest argument: {shortest}")

if __name__ == "__main__":
    main()

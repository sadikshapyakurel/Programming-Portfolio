"""
Report how many command-line arguments were provided excluding the program name.
"""

import sys

def main():
    print(f"Number of arguments provided: {len(sys.argv) - 1}")

if __name__ == "__main__":
    main()

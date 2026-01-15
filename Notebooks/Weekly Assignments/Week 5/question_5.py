"""
Take temperature readings from command line and print max, min, and mean.
"""

import sys

def main():
    temps = sys.argv[1:]
    if not temps:
        print("No temperature values provided.")
        return
    try:
        temps = [float(t) for t in temps]
    except ValueError:
        print("All arguments must be numbers.")
        return
    print(f"Max temperature: {max(temps)}")
    print(f"Min temperature: {min(temps)}")
    print(f"Mean temperature: {sum(temps) / len(temps):.2f}")

if __name__ == "__main__":
    main()

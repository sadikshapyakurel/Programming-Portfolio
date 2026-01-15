"""
Check if a URL is reachable by getting HTTP status code.
Requires 'requests' module.
"""

import sys

try:
    import requests
except ImportError:
    print("Error: 'requests' module not installed. Run 'pip install requests'")
    sys.exit(1)

def main():
    if len(sys.argv) < 2:
        print("Please provide a URL as an argument.")
        return
    url = sys.argv[1]
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            print(f"Website at {url} is reachable (Status code: 200).")
        else:
            print(f"Website at {url} returned status code: {response.status_code}.")
    except requests.RequestException:
        print(f"Website at {url} is not reachable.")

if __name__ == "__main__":
    main()


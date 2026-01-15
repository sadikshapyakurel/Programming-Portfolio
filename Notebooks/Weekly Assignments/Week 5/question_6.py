"""
Take a filename as command-line argument and create a backup copy of that file.
"""

import sys
import os
import shutil

def error(msg):
    print(f"Error: {msg}")
    sys.exit(1)

def backup_file(filename):
    if not os.path.isfile(filename):
        error(f"File '{filename}' does not exist.")
    
    base, ext = os.path.splitext(filename)
    backup_name = f"{base}_backup{ext}"
    
    try:
        shutil.copyfile(filename, backup_name)
        print(f"Backup created: {backup_name}")
    except Exception as e:
        error(f"Failed to create backup: {e}")

def main():
    if len(sys.argv) < 2:
        error("Please provide a filename as an argument.")
    
    filename = sys.argv[1]
    backup_file(filename)

if __name__ == "__main__":
    main()

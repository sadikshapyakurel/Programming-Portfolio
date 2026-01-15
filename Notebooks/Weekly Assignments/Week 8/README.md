## Week 8

## Program 1: Line Number Printer (nl)
Prints the lines of a file with line numbers prepended, similar to the Unix nl command.

It does the following:
- Takes a filename as a command-line argument.
- Opens and reads the file line by line.
- Prints each line preceded by its line number starting at 1.

Key concepts used:
- File handling (open())
- Enumerate function for line numbers
- Command-line arguments (sys.argv)
- Input validation and usage instructions

## Program 2: File Difference Checker (diff)
Compares two text files line by line and prints the differences, similar to the Unix diff command.

It does the following:
- Accepts two filenames as command-line arguments.
- Reads both files into lists of lines.
- Compares corresponding lines, printing differences with line numbers.
- Reports total differences or if files are the same.
- Handles file not found errors gracefully.

Key concepts used:
- File I/O and reading lines
- Exception handling (try/except)
- String manipulation (rstrip)
- Looping over ranges and comparisons
- Counting and reporting differences

## Program 3: Pattern Search in File (grep)
Searches for a specific pattern in a file and prints all lines containing that pattern, similar to the Unix grep command.

It does the following:
- Takes a search pattern and filename as command-line arguments.
- Reads the file line by line.
- Prints lines that contain the given pattern.
- Handles file not found and other exceptions.

Key concepts used:
- File reading line by line
- String containment check (in)
- Exception handling
- Command-line argument parsing

## Program 4: Line and Character Counter (wc)
Counts and displays the number of lines and characters in a file, similar to the Unix wc command.

It does the following:
- Takes a filename as a command-line argument.
- Reads the entire file content.
- Counts lines by counting newline characters.
- Counts total characters.
- Handles file not found errors.

Key concepts used:
- File reading
- String operations (count, len)
- Exception handling
- Command-line arguments

## Program 5: Spell Checker (spell)
ads a file and reports words that are not found in a given dictionary file (dictionary.txt).

It does the following:
- Loads dictionary words into a set for fast lookup.
- Reads input text, removes punctuation, converts to lowercase.
- Checks which words are not in the dictionary.
- Prints unknown words or confirms all words are found.
- Handles missing files and other errors.

Key concepts used:
- File I/O
- Sets for membership testing
- String translation and punctuation removal
- Error handling
- Sorting and printing results

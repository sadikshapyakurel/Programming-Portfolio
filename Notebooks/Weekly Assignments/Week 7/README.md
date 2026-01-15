## Week 7

## Program 1: Unique Sorted Letters from a String
This program takes a string and returns a sorted list of unique letters from that string.
For example, the word "cheese" returns ['c', 'e', 'h', 's'].

It does the following:
- Accepts a string as input.
- Removes duplicate letters using a set.
- Sorts the unique letters alphabetically.
- Prints the final list.

Key concepts used:
- Functions
- Sets (set())
- Removing duplicates
- Sorting (sorted())
- Lists

## Program 2: Letter Comparison Between Two Words
This program uses three functions to compare letters from two words.

It does the following:
- Finds letters that appear in either word.
- Finds letters that appear in both words.
- Finds letters that appear in only one of the words.
- Returns each result as a sorted list.

Key concepts used:
- Functions
- Set operations
   . Union (|)
   . Intersection (&)
   . Symmetric difference (^)
- Sorting
- Lists and sets

## Program 3: Country–Capital Manager
This program manages country–capital pairs.If a country is already known, it prints the capital.
If not, it asks the user to enter and store the capital.The program is case-insensitive.

It does the following:
- Continuously asks the user for a country name.
- Converts input to lowercase for consistency.
- Checks if the country exists in the dictionary.
- Prints the capital if known, otherwise asks and saves it.
- Stops when the user types exit.

Key concepts used:
- Functions
- Dictionaries
- While loop
- User input
- String methods (strip(), lower(), title())
- Conditional statements

## Program 4: Six Most Common Letters in a Message
This program counts letters in a message (case-insensitive) and prints the six most common letters along with their counts.

It does the following:
- Converts the message to lowercase.
- Removes non-letter characters.
- Counts letter frequency.
- Displays the six most frequent letters.

Key concepts used:
- Functions
- List comprehension
- String methods (lower(), isalpha())
- collections.Counter
- Frequency analysis

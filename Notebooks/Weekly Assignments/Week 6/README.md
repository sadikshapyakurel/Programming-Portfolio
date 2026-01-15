## Week 6

## Program 1: Integer to Binary Converter
This program converts a positive integer into its binary representation without the 0b prefix.

It does the following:
- Takes an integer value.
- Uses Python’s built-in binary conversion.
- Removes the 0b prefix from the result.
- Prints the binary number.

Key concepts used:
- Functions
- Built-in function bin()
- String slicing
- Integer handling

## Program 2: Factor Finder
This program returns all factors of a given number as a list.

It does the following:
- Iterates from 1 to the given number.
- Checks which numbers divide evenly.
- Stores valid factors in a list.
- Returns and prints the list of factors.

Key concepts used:
- Functions
- for loop
- Modulus operator (%)
- Lists

## Program 3: Prime Number Checker
This program checks whether a given integer is a prime number.

It does the following:
- Handles edge cases (numbers ≤ 1).
- Checks divisibility only up to the square root of the number.
- Returns True if prime, otherwise False.
- Demonstrates results using test values.

Key concepts used:
- Functions
- Conditional statements
- for loop
- Mathematical optimization (n**0.5)
- Boolean return values

## Program 4: Simple Message Encryption (Reverse Method)
This program encrypts a message by removing spaces and reversing the string.

It does the following:
- Removes all spaces from the message.
- Reverses the remaining characters.
- Returns and prints the encrypted message.

Key concepts used:
- Functions
- String methods (replace())
- String slicing ([::-1])

## Program 5: Hidden Message Encryption with Random Letters
This program encrypts a message by inserting random letters between each character at a random interval.

It does the following:
- Removes spaces from the message.
- Generates a random interval between 2 and 20.
- Inserts random lowercase letters between message characters.
- Returns the encrypted message and interval used.

Key concepts used:
- Functions
- Random module
- string module
- Loops
- String manipulation
- Tuple return values

## Program 6: Message Decryption
This program decrypts a message that was encrypted using the hide_message function.

It does the following:
- Takes the encrypted message and interval value.
- Extracts every nth character based on the interval.
- Reconstructs and prints the original message.

Key concepts used:
- Functions
- String indexing
- Range() with step values
- Loops

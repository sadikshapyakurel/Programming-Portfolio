# Week 3

## Program 1: Greet User by Name
Greets the user by name. If the user enters no name (empty input), it greets them as "Stranger".                                           
It does the followings:                                                                                                               - Prompts for the user's name.
- Uses a conditional expression to check if the input is empty.
- Prints a personalized greeting or "Stranger" if no name is given.                                                                                                                   
Key concepts used:
- User input (input())
- String manipulation (strip())
- Conditional expressions (ternary operator)
- String formatting (f-strings)

## Program 2: Password Match Check                                                                                                    
prompts the users to enter a password twice and checks if both entries match.

It does the followings:                                                                                                              - Takes two password inputs from the user.
- Compares the two entries.
- Prints confirmation if passwords match or an error message if they don’t.

Key concepts used:
- User input (input())
- String comparison
- Conditional expression (ternary operator)

## Program 3: Password Validation with Length Check                                                                                   
Checks if the password entries match and whether the password length is between 8 and 12 characters.

It does the following:
- Takes two password inputs.
- Checks if both passwords match and the length is within the valid range.
- Prints "Password set" if valid; otherwise, prints an error.

Key concepts used:
- User input (input())
- String comparison
- Logical operators (and)
- Length check (len())
- Conditional expressions

## Program 4: Password Validation with Common Password Prevention                                                                   
Extends password validation to prevent common weak passwords
It does the following:
- Uses a predefined list of bad passwords.
- Validates passwords like Program 3, but also ensures the password is not in the bad password list.
- Prints appropriate success or error messages.

Key concepts used:
- Lists
- Membership testing (not in)
- Logical operators and conditional expressions
- User input and string operations

## Program 5:  Password Entry Loop Until Valid                                                                                        
Repeats password entry until the user chooses a valid password (matching, correct length, and not common).

It does the following:
- Uses a while True loop to keep asking for passwords until they meet all criteria.
- Provides feedback on invalid passwords.
- Exits loop and confirms when a valid password is entered.

Key concepts used:
- Infinite loops (while True)
- Break statement
- Input validation
- Lists and membership testing
- Logical operators

## Program 6: Seven Times Table
Displays the 7 times multiplication table from 0 to 12.

It does the folllowing:
- Uses a for loop to iterate through numbers 0 to 12.
- Prints each product formatted as a multiplication statement.

Key concepts used:
- for loops and range()
- Arithmetic operations
- String formatting (f-strings)

## Program 7: User-Selected Times Table
Displays a times table based on a number entered by the user between 0 and 12.

It does the following:
- Prompts the user for a number.
- Prints the multiplication table for that number from 0 to 12.

Key concepts used:
- User input and type conversion (int())
- Loops (for and range())
- Arithmetic and string formatting

## Program 8: Times Table with Backward Option
Prints a times table. If the user enters a negative number, the table is printed backwards from 12 to 0.

It does the following:
- Takes an integer input from the user.
- Uses the absolute value for multiplication.
- Decides the sequence direction based on the sign of the input.
- Prints the times table accordingly.

Key concepts used:
- User input and type conversion
- Conditional logic (if statement)
- Range() with different steps
- Absolute value (abs())
- Looping and string formatting


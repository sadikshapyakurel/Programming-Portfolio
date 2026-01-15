## Week 5

## Program 1: Operating System Platform Reporter
This program reports the operating system platform on which the script is executed.

It does the following:
- Uses the sys module to identify the OS platform.
- Prints the platform information when run from the command line.

Key concepts used:
- sys module
- Functions
- __name__ == "__main__"
- Command-line execution

## Program 2: Command-Line Argument Counter
This program reports how many command-line arguments were provided, excluding the program name itself.

It does the following:
- Reads command-line arguments using sys.argv.
- Counts the number of arguments passed by the user.
- Displays the total count.

Key concepts used:
- sys.argv
- Lists
- Functions
- Command-line arguments

## Program 3: Shortest Command-Line Argument Finder
This program prints the shortest command-line argument provided by the user.If multiple arguments are equally
short, any one of them may be printed.

It does the following:
- Extracts command-line arguments excluding the program name.
- Checks if any arguments were provided.
- Finds and prints the shortest argument.

Key concepts used:
- Command-line arguments
- Lists and slicing
- Built-in functions (min())
- String length (len())

## Program 4: Website Reachability Checker
This program checks whether a given URL is reachable by retrieving its HTTP status code.
It requires the external requests module.

It does the following:
- Accepts a URL as a command-line argument.
- Sends an HTTP GET request to the URL.
- Reports whether the website is reachable and displays the status code.
- Handles missing modules and connection errors.

key concepts used:
- External modules (requests)
- Exception handling (try / except)
- Command-line arguments
- HTTP status codes

## Program 5: Temperature Statistics from Command Line
This program takes temperature readings from the command line and prints the maximum, minimum, and mean values.

It does the following:
- Reads numeric values from command-line arguments.
- Converts inputs to floating-point numbers.
- Calculates and prints max, min, and mean temperature.
- Handles invalid input errors.

Key concepts used:
- Command-line arguments
- Lists
- Type conversion (float)
- Built-in functions (max(), min())
- Arithmetic operations
- Error handling

## Program 6: File Backup Creator
This program takes a filename as a command-line argument and creates a backup copy of the file.

It does the following:
- Checks whether the file exists.
- Creates a backup file with _backup added to the filename.
- Copies the file contents safely.
- Handles file and argument errors.

Key concepts used:
- File handling
- os module
- shutil module
- Functions
- Error handling and program exit (sys.exit())

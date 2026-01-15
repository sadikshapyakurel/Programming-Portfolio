"""
This program asks for the number of students
It calculates how many groups can be formed and
remaining using integer division and the modulus
"""
number_of_students = int(input("How many students? "))
group_size = int(input("Required group size? "))

groups = number_of_students // group_size
leftover = number_of_students % group_size

word = "student" if leftover == 1 else "students"

print(f"There will be {groups} groups with {leftover} {word} left over.")

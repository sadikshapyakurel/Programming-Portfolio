total_sweets = int(input("How many sweets are there? "))
pupils = int(input("How many pupils are present? "))

each = total_sweets // pupils
leftover = total_sweets % pupils

word = "sweet" if leftover == 1 else "sweets"

print(f"Each pupil gets {each} sweets with {leftover} {word} left over.")

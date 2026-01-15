"Program to manage country-capital pairs. If country known, print capital; else ask and save it. Case-insensitive."
def manage_countries():
    capitals = {}
    while True:
        country = input("Country (or 'exit'): ").strip().lower()
        if country == "exit":
            break
        if country in capitals:
            print(f"Capital of {country.title()} is {capitals[country]}")
        else:
            capital = input(f"Enter capital of {country.title()}: ").strip()
            capitals[country] = capital

manage_countries()  


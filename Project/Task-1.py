# Simple pizza price calculator - student version
print("Beckett Pizza Plaza 4-for-3 Offer")
print("=================================")
print()


# Pizza 1
ok = False
while ok == False:
    try:
        price1 = float(input("Enter Price of Pizza #1: "))
        if price1 > 0:
            ok = True
        else:
            print("Please enter a valid price!")
    except:
        print("Please enter a valid price!")


# Pizza 2
ok = False
while ok == False:
    try:
        price2 = float(input("Enter Price of Pizza #2: "))
        if price2 > 0:
            ok = True
        else:
            print("Please enter a valid price!")
    except:
        print("Please enter a valid price!")


# Pizza 3
ok = False
while ok == False:
    try:
        price3 = float(input("Enter Price of Pizza #3: "))
        if price3 > 0:
            ok = True
        else:
            print("Please enter a valid price!")
    except:
        print("Please enter a valid price!")


# Pizza 4
ok = False
while ok == False:
    try:
        price4 = float(input("Enter Price of Pizza #4: "))
        if price4 > 0:
            ok = True
        else:
            print("Please enter a valid price!")
    except:
        print("Please enter a valid price!")


# Put all prices in a list
all_prices = [price1, price2, price3, price4]


# Find the cheapest pizza
cheapest = all_prices[0]
if price2 < cheapest:
    cheapest = price2
if price3 < cheapest:
    cheapest = price3
if price4 < cheapest:
    cheapest = price4


# Calculate total (pay for 3 most expensive = all minus cheapest)
original_total = price1 + price2 + price3 + price4
pay_total = original_total - cheapest


# Calculate discount percentage
if original_total > 0:
    discount_amount = original_total - pay_total
    discount_percent = (discount_amount / original_total) * 100
    discount_percent = round(discount_percent)
else:
    discount_percent = 0


# Show result
print()
print(f"Order Total is £{pay_total:.2f}, a fabulous discount of {discount_percent}%!")


# Optional: Show which pizza was free
print("(The £" + f"{cheapest:.2f}" + " pizza was free!)")
print()
print("Thank you for choosing Beckett Pizza Plaza!")
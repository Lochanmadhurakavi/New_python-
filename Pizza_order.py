print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ").lower()
add_pepperoni = input("Do you want pepperoni? Y or N ").lower()
extra_cheese = input("Do you want extra cheese? Y or N ").lower()

final_bill = 0
if size == "s":
    final_bill += 15
    if add_pepperoni == "y":
        final_bill += 2
elif size == "m":
    final_bill += 20
    if add_pepperoni == "y":
        final_bill += 3
elif size == "l":
    final_bill += 25
    if add_pepperoni == "y":
        final_bill += 3
if extra_cheese == "y":
    final_bill += 1

print(f"Your final bill is: ${final_bill}")

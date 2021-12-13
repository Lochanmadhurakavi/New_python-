total_amount = 0

height = int(input("Enter your height:"))

if height > 120:
    print("Yes, You can ride")
    age = int(input("Enter your age:"))
    if age < 12:
        total_amount += 5
    elif 12 <= age < 18:
        total_amount += 7
    elif age >= 18:
        total_amount += 12
    want_photos = input("Do you want photos? Type yes or no:").lower()
    if want_photos == "yes":
        total_amount += 3
    elif want_photos == "no":
        print("Ok, You don't want photos")
    print(f"Your total amount equal to {total_amount}")

else:
    print("Sorry, You cant ride grow taller!")

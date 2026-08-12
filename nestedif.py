age=20

if age>=18:
    if age>=21:
        print("you can vote")
    else:
        print("you cannot vote")
else:
    print("your age is not greater than or equal to 18")

choice = int(input("Enter your choice (1-2): "))
if choice == 1:
    bike_type = int(input("enter 1 or 2:"))
    if bike_type == 1:
        print("You picked a sports bike")
    else:
        print("You did not choose a sports bike")
elif choice == 2:
    print("You picked a cruiser bike")


id_card = input("Do you have an ID card? yes/no")
if id_card.lower() == "yes":
    id_valid = input("Is your id card valid? yes/no")
    if id_valid.lower() == "yes":
        print("You can enter the school")
    else:
        print("you cannot enter the school")
else:
    print("you cannot enter the school")
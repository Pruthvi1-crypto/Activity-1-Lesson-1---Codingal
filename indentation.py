temperature = int(input("Enter the temperature in celsius: "))
if temperature < 20:

    outfit = "Jaket"
    print("It is cold today")
    print("You should wear a", outfit)

else:
    outfit = "T-shirt"
    print("It is very hot today")
    print("You should wear a", outfit)

age = int(input("Enter your age: "))
if age < 18:
    print("You are a minor")
    print("You are not allowed to vote")

else:
    print("You are a adult")
    print ("You are allowed to vote")

name = input("Enter your name")
if name == "Pruthvi Raj Chauhan":
    print("You are the king of India", name)
    print("You are a great karate king", name)
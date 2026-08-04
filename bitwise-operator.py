print("Enter marks obtained in 5 subjects")
marks1 = int(input())
marks2 = int(input())
marks3 = int(input())
marks4 = int(input())
marks5 = int(input())

total = marks1 + marks2 + marks3 + marks4 + marks5
average = int(total / 5)
print(average)
valid_range = range(0, 101)

if average not in valid_range:
    print("Invalid input. Please enter marks between 0 and 100.")
elif average in range(60, 101):
    print("Your Grade is A")
elif average in range(81, 91):
    print("Your Grade is B") 
else:
    print("Your Grade is C")
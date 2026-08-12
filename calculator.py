name = input("What is your name?")
print("hello", name)
number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number:  "))
operation = input("Choose operation +, -, *, /: ")
if operation == "A":
    print(number1 + number2)
elif operation == "S":
    print(number1 - number2)
elif operation == "D":
    print(number1 * number2)
elif operation == "W":
    print(number1 / number2)
else: 
    print("invalid operation") 
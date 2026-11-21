name = input("What is your name?")
print("Hallo", name)
number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))
operation = input("Choose operation: +, -, *, /, %, R, C, P, M, B: ")
if operation == "+":
    result = number1 + number2 
    print(result)
elif operation == "-":
    result = number1 - number2
    print(result)
elif operation == "*":
    result = number1 * number2
    print(result)
elif operation == "/":
    if number2 == 0:
        print("Error: Cannot divide by zero!")
    else:
        result = number1 / number2
        print(result)
elif operation == "%":
    result = number1 % number2
    print(result)
elif operation == "R":
    if number1 % 2 == 0:
        print("Even")
    else: 
        print("Odd")
elif operation == "C":
    if number1 > number2:
        print("First number is bigger")
    elif number1 < number2:
        print("First number is smaller")
    else:
        print("Numbers are equal")
elif operation == "P":
    if number1 > 0 and number2 > 0:
        print("Both numbers are positive")
    elif number1 > 0 or number2 > 0:
        print("At least one number is positive")
    else:
        print("No positive numbers") 
elif operation == "M":
    if number1 != 0:
        print("Number is not zero")
    else:
        print("Number is zero")
elif operation == "B":
    is_bigger = number1 > number2
    print(is_bigger)
else: 
    print("invalid operation")
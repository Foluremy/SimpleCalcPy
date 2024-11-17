num1 = int(input("Input a number: "));

num2 = int(input("Input another number: "));

operator = input("Choose an operator (+, -, *, /): ");

# Perform the operation
if operator == "+":
    result = num1 + num2
    print(f"The result of {num1} + {num2} is: {result}")
elif operator == "-":
    result = num1 - num2
    print(f"The result of {num1} - {num2} is: {result}")
elif operator == "*":
    result = num1 * num2
    print(f"The result of {num1} * {num2} is: {result}")
elif operator == "/":
    if num2 != 0:
        result = num1 / num2
        print(f"The result of {num1} / {num2} is: {result}")
    else:
        print("Error: Division by zero is not allowed.")
else:
    print("Invalid operator. Please choose +, -, *, or /.")
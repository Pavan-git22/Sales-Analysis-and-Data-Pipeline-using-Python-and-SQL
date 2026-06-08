number1 = float(input("Enter the first number: "))
number2 =float(input("Enter the second number: "))

operation = input("Enter the operation (+, -, *, /): \n")
if operation == "+":
    print(f"the result of {number1} + {number2} is: {number1 + number2}")
elif operation == "-":
    print(f"the result of {number1} - {number2} is: {number1 - number2}")
elif operation == "*":
    print(f"the result of {number1} * {number2} is: {number1 * number2}")
elif operation == "/":
    print(f"the result of {number1} / {number2} is: {number1 / number2}")
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    else:
        return x / y

def calculator():
    operations = {
        '1': add,
        '2': subtract,
        '3': divide
    }

    print("Select operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Division")

    choice = input("Enter choice (1/2/3): ")

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice in operations:
        result = operations[choice](num1, num2)
        print("Result:", result)
    else:
        print("Invalid input")

calculator()

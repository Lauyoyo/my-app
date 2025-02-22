def calculator():
    print("Simple calculator")
    num1 = float(input("Enter the first number: "))
    operation = input("Select operation (+, -, *, /): ")
    num2 = float(input("Enter the second number: "))

    if operation == '+':
        print(f"result: {num1 + num2}")
    elif operation == '-':
        print(f"result: {num1 - num2}")
    elif operation == '*':
        print(f"result: {num1 * num2}")
    elif operation == '/':
        if num2 != 0:
            print(f"result: {num1 / num2}")
        else:
            print("Error: The divisor cannot be zero")
    else:
        print("Invalid operation")

if __name__ == "__main__":
    calculator()
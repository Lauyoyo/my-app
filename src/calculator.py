import os

def calculator():
    print("Simple calculator")

    num1 = float(os.getenv("NUM1", 1))  # Read environment variable, default 1
    operation = os.getenv("OPERATION", "+")
    num2 = float(os.getenv("NUM2", 2))

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

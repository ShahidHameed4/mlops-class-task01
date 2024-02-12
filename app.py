# main.py

def add_numbers(a, b):
    return a + b

def subtract_numbers(a, b):
    return a - b

def multiply_numbers(a, b):
    return a * b

def divide_numbers(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b

if __name__ == "__main__":
    num1 = 10
    num2 = 5

    print(f"Addition: {add_numbers(num1, num2)}")
    print(f"Subtraction: {subtract_numbers(num1, num2)}")
    print(f"Multiplication: {multiply_numbers(num1, num2)}")
    print(f"Division: {divide_numbers(num1, num2)}")

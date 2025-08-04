import sys

# Here i add Function to add all numbers and so on..
def add(numbers):
    return sum(numbers)

#subtract
def subtract(numbers):
    result = numbers[0]
    for num in numbers[1:]:
        result -= num
    return result

#multiply
def multiply(numbers):
    result = 1
    for num in numbers:
        result *= num
    return result

#divide
def divide(numbers):
    result = numbers[0]
    try:
        for num in numbers[1:]:
            result /= num
    except ZeroDivisionError:
        return "Error: Division by zero is not allowed."
    return result

# Function to perform the operation
def calculate(operation, numbers):
    if operation in ["add","addition"]:
        return add(numbers)
    elif operation in ["sub","subtract"]:
        return subtract(numbers)
    elif operation in ["mul","multiply","multiplication"]:
        return multiply(numbers)
    elif operation in ["div","divide","division"]:
        return divide(numbers)
    else:
        return "Error: Invalid operation."

# Main program block
if __name__ == "__main__":
    try:
        operation = sys.argv[1]
        numbers = [float(num) for num in sys.argv[2:]]
        
        if len(numbers) < 2:
            print("Error: Please provide at least two numbers.")
        else:
            result = calculate(operation, numbers)
            print(f"Result: {result}")
    except IndexError:
        print("Usage: python calculator.py [operation] [num1] [num2] ...")
        print("Example: python calculator.py add 10 20 30")
    except ValueError:

        print("Error: Please enter valid numeric values only.")

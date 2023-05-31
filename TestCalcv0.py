# This code is a Python mimic of @FlamesLLC on Github

# Import required module
import sys

# Function to add two numbers
def add(num1, num2):
    return num1 + num2

# Function to subtract two numbers
def subtract(num1, num2):
    return num1 - num2

# Function to multiply two numbers
def multiply(num1, num2):
    return num1 * num2

# Function to divide two numbers
def divide(num1, num2):
    if num2 == 0:
        print("Error! Division by zero is not allowed.")
        return
    else:
        return num1 / num2

def main():
    # Check if the right number of command line arguments are provided
    if len(sys.argv) != 4:
        print("Usage: python3 calculator.py [num1] [operator] [num2]")
        sys.exit(1)
    
    # Get the numbers and operator from command line arguments
    num1, operator, num2 = float(sys.argv[1]), sys.argv[2], float(sys.argv[3])
    
    # Perform the appropriate operation based on the operator
    if operator == "+":
        result = add(num1, num2)
    elif operator == "-":
        result = subtract(num1, num2)
    elif operator == "*":
        result = multiply(num1, num2)
    elif operator == "/":
        result = divide(num1, num2)
    else:
        print(f"Error! Operator '{operator}' is not supported.")
        sys.exit(1)
    
    # Print the result
    print(f"The result is: {result}")

# Call the main function
if __name__ == "__main__":
    main()

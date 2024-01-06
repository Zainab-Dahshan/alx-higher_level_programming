#!/usr/bin/python3
# Import functions from calculator_1.py
from calculator_1 import add, subtract, multiply, divide
# Definition of the variables a and b
if __name__ == "__main__":
a = 10
b = 5
# Calling each of the imported functions
result_add = add(a, b)
result_subtract = subtract(a, b)
result_multiply = multiply(a, b)
result_divide = divide(a, b)
# Printing the results
print("Result of addition:", result_add)
print("Result of subtraction:", result_subtract)
print("Result of multiplication:", result_multiply)
print("Result of division:", result_divide)


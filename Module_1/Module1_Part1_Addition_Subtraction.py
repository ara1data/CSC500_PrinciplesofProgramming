# Part 1 Assignment Prompt:
'''
Write a Python program to find the addition and subtraction of two numbers.
Ask the user to input two numbers (num1 and num2). Given those two numbers, 
add them together to find the output. Also, subtract the two numbers to find the output.
'''
# ---------------------------------------------

# Define Number Variables and Prompt User for Input
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Addition and Subtraction Function
addition_result = num1 + num2
subtraction_result = num1 - num2

# Print Addition and Subtraction Results
print(f"The addition of {num1} and {num2} is: {addition_result}")
print(f"The subtraction of {num2} from {num1} is: {subtraction_result}")
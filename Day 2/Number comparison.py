"""
Number Comparison
Create a program that asks the user to enter two numbers.
Print "The first number is larger" if the first number is greater,
"The second number is larger" if the second number is greater,
 and "Both numbers are equal" if they are the same.
"""

# Get two numbers from the user
num1 = int(input("Enter First Number: "))
num2 = int(input("Enter Second Number: "))
if num1 > num2:
    print("The First Number is Larger")
elif num1 < num2:
    print("The Second Number is Larger")
else:
    print("Both Number are Equal")
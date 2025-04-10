# if else print if statement, we can use manu if in a program with out else
# we can use many elif also, but once we used else in the bottom of the program we cant able to use any if or elif

csk = "win"
if(csk == "win"):
    print("IPL Champions")
else:
    print("Cup illa, Bulb")

# if else print else statement
csk = "lose"
if(csk == "win"):
    print("IPL Champions")
else:
    print("Cup illa, Bulb")

# Another Example
meghna = input("meghna died or not")
if(meghna =="Died"):
    print("suriya meet priya")
else:
    print("suriya weds meghna")


# Get input for variable mark,if mark >35 print pass, else fail
mark = int(input("Enter the mark: "))
if(mark>35):
    print("pass")
else:
    print("fail")

# Get input for variable income, income >7000 scholarship available else  not eligible for scholarship
income = int(input("Enter Your income: "))
if(income>7000):
    print("Scholarship is available")
else:
    print("Scholarship not available")

# Get input for number, divisible by 3 using binary operator and or not
number = int(input("Enter the number: "))
if(number%3 == 0 and number%5 == 0):
    print("divisible by 3 and 5")
else:
    print("Not divisible by 3 and 5")

# Get input for number, find even or odd
number = int(input("Enter the Number: "))
if(number%2==0):
    print("Even Number")
else:
    print("odd Number")


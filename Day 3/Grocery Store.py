# Get total value of Grocery as input, if total >500 10% discount, if Total less then 500 - no discount
# total >1000- 20 % discount

print("Grocery Discount Alert! Maximum discount applicable for bill value of Rs: 10000🤴")

# Declare variable for Total
total = int(input("Enter final bill Amount Rs: "))

if total > 10000:
    print("You Are Eligible for 50% Discount")
    name = input("Enter your Name: ")
    Mail = input("Enter your Email: ")
    phone = int(input("Enter your phone number: "))
    Address = input("Enter Your Address: ")
    print("😀 Thank you 😀")
elif total > 7500:
    print("You Are Eligible for 40% Discount")
    name = input("Enter your Name: ")
    Mail = input("Enter your Email: ")
    phone = int(input("Enter your phone number: "))
    Address = input("Enter Your Address: ")
    print("😀 Thank you 😀")
elif total > 5000:
    print("You Are Eligible for 30% Discount")
    name = input("Enter your Name: ")
    Mail = input("Enter your Email: ")
    phone = int(input("Enter your phone number: "))
    Address = input("Enter Your Address: ")
    print("😀 Thank you 😀")
elif total > 1000:
    print("You Are Eligible for 10% Discount")
    name = input("Enter your Name: ")
    Mail = input("Enter your Email: ")
    phone = int(input("Enter your phone number: "))
    Address = input("Enter Your Address: ")
    print("😀 Thank you 😀")
elif total > 500:
    print("You Are Eligible for 5% Discount")
    name = input("Enter your Name: ")
    Mail = input("Enter your Email: ")
    phone = int(input("Enter your phone number: "))
    Address = input("Enter Your Address: ")
    print("😀 Thank you 😀")
else:
    print("You Are Not Eligible for Discount")

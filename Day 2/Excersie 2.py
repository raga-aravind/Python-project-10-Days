"""
Another example for if statements
Get input for salary and age salary >=20000 or age <=25 get input for required loan if not not eligible
loan amt is <=50000 your eligible, >50000 print maximum loan amt is 50000.
"""

# nested if
print("Loan Eligibility Check Application")
# salary details
salary = int(input("Enter Your Monthly Salary Rs: "))
age = int(input("Enter your present age: "))
if salary < 20000 and age > 25:
    print("Your Not eligible")
else:
        print("your are eligible, please input the Required loan amount")
        loan = int(input("Enter the Required loan amount Rs: "))
        if loan <= 50000:
         print(f"your Are Eligible for loan Rs: {loan} ")
        elif loan > 50001:
            print("Maximum loan eligibility is Rs : 50000")
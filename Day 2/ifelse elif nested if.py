
# Get input as score from variable, score<35 print poor student, score>35 and score<70 average, score>70 good
score = int(input("Enter the Mark: "))
if score < 35:
    print("Very poor Student need to improve")
elif score >= 35 and score <= 70:
    print("Average student need to do better")
elif score > 70 and score <=100:
    print("good Student")
else:
    print("Invalid Input- Enter Number with in 100")

# mini calculator, get input from user for a &b
a = int(input("Enter the Value For A : "))
b = int(input("Enter The Value For B : "))
operation = input("Enter the Operation value : add/sub/mul/div ")
if operation == "add":
    print(a+b)
elif operation == "sub":
    print(a-b)
elif operation == "mul":
    print(a*b)
elif operation == "div":
    print(a/b)
else:
    print("invalid operation")

# Get score percentage as input, >70 means get input as name location department
print("Scholarship eligibility check")
score = int(input("Enter Your Score : "))
if score < 70:
    print("your Are Not eligible")
elif score >= 70 :
    print("your Are  eligible! please fill the below details")
    name = input("Enter your Name: ")
    location = input("Enter Your Location: ")
    department = input("Enter Your Department: ")
    print("Thank you")
else:
    print("Invalid Details")
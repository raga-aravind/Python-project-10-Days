# Grt input for number a and number b
# print the number between a and b
"""
print("Print the number between given number")
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
for i in range(a+1,b):
    print(i)


# print even number between 1 to 10
print("Print even number between 1 To 10")
for i in range(1 , 11):
    if i % 2 == 0:
       print(i)
"""
# count of even number
print("Print even number between 1 To 10")
count = 0
for i in range(1,11):
    if i % 2 == 0:
        count+=1
        print(i)
        print(f"Total even numbers: {count}")
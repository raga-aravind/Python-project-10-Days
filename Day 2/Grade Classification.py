"""
Write a program that asks the user to input a score between 0 and 100. Based on the score, print the grade:
"A" for scores 90 and above
"B" for scores between 80 and 89
"C" for scores between 70 and 79
"D" for scores between 60 and 69
"""
print("Grade Classification")
# Get the score from the user
grade = int(input("Enter the Mark between 0 to 100: "))
# Determine the grade
if grade >= 90:
    print("Grade A")
elif grade >= 80 and grade <= 89:
    print("Grade B")
elif grade >= 70 and grade <= 79:
    print("Grade C")
elif grade >=60 and grade <= 69:
    print("Grade D")
else:
    print("Grade F")

# Another Method
# Get the score from the user
score = int(input("Enter your score (0-100): "))

# Determine the grade
if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
elif score >= 60:
    print("Grade: D")
else:
    print("Grade: F")

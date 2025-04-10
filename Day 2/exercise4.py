"""
Write a program that determines if someone is eligible to vote.
Ask the user for their age. If they are 18 or older, print "You are eligible to vote." Otherwise,
print "You are not eligible to vote."
"""

# Ask the user to input their age
age = int(input("Enter The Age: "))
# Check voting eligibility
if age >= 18:
    print("Your Eligible to VOTE")
else:
    print("Your Not Eligible to VOTE")
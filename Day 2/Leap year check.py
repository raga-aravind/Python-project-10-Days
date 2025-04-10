# Ask the user to input a year. Determine if the year is a leap year:
# A year is a leap year if it's divisible by 4, but not divisible by 100, unless it's also divisible by 400.


# Get the year from the user
year = int(input("Enter a year: "))

# Check if it's a leap year
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")

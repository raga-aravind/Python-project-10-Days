"""
Bill Splitting Helper
Write a program that helps split a restaurant bill based on group size:
If group size is 2, suggest splitting equally.
If group size is 3 or 4, suggest assigning shares based on individual orders.
If group size is greater than 4, suggest dividing equally with a service charge.
If group size is 1, suggest paying the full bill.
"""
print("Bill Splitting Helper")

# Input for group size
group_size = int(input("Size of the group: "))

# Decision structure
if group_size == 2:
    print("Suggest splitting equally.")
elif 3 <= group_size <= 4:  # More concise condition
    print("Suggest assigning shares based on individual orders.")
elif group_size > 4:
    print("Suggest dividing equally with a service charge.")
else:  # Covers group size of 1 or invalid input
    print("Suggest paying the full bill.")

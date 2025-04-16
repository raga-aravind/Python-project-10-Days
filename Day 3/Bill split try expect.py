"""
Updated Program:
Error Handling: We'll validate the input to ensure the group size is a positive integer.
Cost Calculation: We'll prompt the user for the total bill amount and calculate the per-person share based on the splitting method.
Tip Suggestions: We'll add a feature to recommend tips at 10%, 15%, and 20% of the total bill.
"""

print("Bill Splitting Helper")

try:
    # Input for group size
    group_size = int(input("Enter the size of the group: "))

    # Check for valid group size
    if group_size <= 0:
        print("Group size must be a positive number. Please try again.")
    else:
        # Input for total bill amount
        total_bill = float(input("Enter the total bill amount (Rs): "))

        # Decision structure
        if group_size == 2:
            print("Suggest splitting equally.")
            share = total_bill / group_size
            print(f"Each person should pay: Rs {share:.2f}")
        elif 3 <= group_size <= 4:
            print("Suggest assigning shares based on individual orders.")
            print("Each person can calculate their share based on their orders.")
        elif group_size > 4:
            print("Suggest dividing equally with a service charge.")
            service_charge = 0.10 * total_bill  # Example: 10% service charge
            total_with_charge = total_bill + service_charge
            share = total_with_charge / group_size
            print(f"A 10% service charge is applied. Total with service charge: Rs {total_with_charge:.2f}")
            print(f"Each person should pay: Rs {share:.2f}")
        else:
            print("Suggest paying the full bill.")
            print(f"Total bill amount: Rs {total_bill:.2f}")

        # Tip suggestions
        print("\nRecommended tips:")
        for tip_percent in [10, 15, 20]:
            tip_amount = (tip_percent / 100) * total_bill
            print(f"{tip_percent}% tip: Rs {tip_amount:.2f}")

except ValueError:
    print("Invalid input. Please enter a valid number.")

# Welcome to the "Pet Shop Adventure" exercise!

# Step 1: Declare variables for your pet shop
shop_name = "Happy Tails Pet Shop"
owner_name = "Alex"
pet_type = "dog"
pet_count = 10
pet_price = 120.50

# Step 2: Print some basic details using the variables
print("Welcome to", shop_name + "!")
print("Today's special offer: Buy a", pet_type, "for just", pet_price, "USD!")
print("We have", pet_count, pet_type + "s in stock.")
print("Meet", owner_name + ", the proud owner of the shop.")

# Step 3: Update the pet count and calculate total revenue
sold_pets = 3
pet_count = pet_count - sold_pets
total_revenue = sold_pets * pet_price

# Step 4: Display the updated pet count and revenue
print("After selling", sold_pets, pet_type + "s, we now have", pet_count, pet_type + "s left.")
print("Total revenue for today is:", total_revenue, "USD.")





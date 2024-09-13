# Gemma Tipping
# Homework Assignment 1
# Last Modified: 09/12/2024

# Main Context: The Python program I have created simulates an inventory system for a beauty
# store such as Sephora or Ulta. The idea is that employees can run this program to check on
# certainproducts that the beauty store sells and once a certain "threshold" is hit, the program
# will notify the user (based on their input) that that item needes to be reordered. Otherwise,
# the program will notify the user that no order is necessary.

# For the use of a compound data data type, I will use a dictionary to store how much inventory
# is left for specific items
inventory = {"moisturizer": 37, "blush": 6, "toner": 68, "shampoo": 19, "mascara": 25, "brush": 0}
reorder_threshold = 24

# Now the program will ask the user to input the product they want to check inventory on
product = input("Enter the name of the product you are checking: ").lower()

# Before moving forward, the program will check the product entered is in inventory (if it is, it
# will check quantity)
if product in inventory:
    quantity = inventory[product]

# Now I have created if statements to compare the actual quantity to the reorder threshold and
# let the user know whether or not they need to reorder
    if quantity == 0:
        print("Oh no! " + product.capitalize() + " is fully out of stock! Reorder today!")
    elif quantity <= reorder_threshold:
# NOTE: A nested if is being added because the item blush is seasonal and won't need reordering
        if product == "blush":
            print(product.capitalize() + " does not need to be reordered at this time.")
        else:
            print(product.capitalize() + " is running low. Reorder this product soon.")
    else:
        print(product.capitalize() + " is sufficiently stocked for now!")
else:
    print("This item is not in the store's inventory! Please enter a new input.")
    
        


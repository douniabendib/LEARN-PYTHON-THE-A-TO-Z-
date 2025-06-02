"""
Create a function named check_inventory that takes two parameters: 
inventory (a dictionary where keys are item names and values 
are quantities) and item (a string representing the item to check). 
The function should:

Check if the item is in the inventory.
If the item is in stock, return the string: "<item> is in stock. 
Quantity: <quantity>".
If the item is not in stock, return the string: "<item> is not in stock."
"""
def check_inventory(inventory, item):
    if item in inventory:
        return f"{item} is in stock. Quantity: {inventory[item]}"
    else:
        return f"{item} is not in stock."


print(check_inventory({"apple":10,"banana":5,"orange":7}, "banana"))

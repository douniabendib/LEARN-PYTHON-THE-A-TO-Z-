"""
Create a program that simulates a shopping cart with error handling. 
Your task is to:
1- Create a function called handle_shopping_cart that processes 
  customer orders
2- The function should accept a list of order strings in the format 
  "item:quantity"
3- Process each order by:
   - Splitting the input string to get the item and quantity
   - Converting the quantity to an integer
   - Adding the item to a shopping cart dictionary with the quantity 
     as value
   - If an item already exists in the cart, update its quantity
4- Handle these specific errors:
   -If the input format is incorrect (missing colon), 
    print "Invalid format: {order}"
   -If the quantity is not a valid number, 
    print "Invalid quantity: {order}"
   -If the quantity is negative, 
    print "Negative quantity not allowed: {order}"
5- Return the completed shopping cart dictionary
"""
def handle_shopping_cart(orders):
    # Create an empty dictionary for the shopping cart
    shopping_cart = {}
    
    # Process each order in the list
    for order in orders:
        try:
            # Split the order and add to cart
            item, quantity_str = order.split(":")
            # Converting the quantity to an integer
            quantity = int(quantity_str)

            # Check for negative quantities
            if quantity < 0:
                print(f"Negative quantity not allowed: {order}")
                continue
            # Add to cart (accumulate the quantities)
            if item in shopping_cart:
               shopping_cart[item] += quantity  # Accumulate quantity if item exists
            else:
               shopping_cart[item] = quantity

        except ValueError:
            if ":" not in order:
                print(f"Invalid format: {order}")
            else:
                print(f"Invalid quantity: {order}")

        except Exception as e:
            print(f"Error processing order: {order}. Reason: {e}")
    return shopping_cart

print(handle_shopping_cart(["apple:3","banana:2","milk:5"]))
print(handle_shopping_cart(["cereal:1","cereal:3","orange:5","butter:2"]))
print(handle_shopping_cart(["bread:2","banana:five","eggs:10"]))
print(handle_shopping_cart(["chocolate:-5","yogurt:3","milk:2"]))

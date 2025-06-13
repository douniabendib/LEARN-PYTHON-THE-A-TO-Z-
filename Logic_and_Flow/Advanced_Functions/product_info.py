"""
Create a function named get_product_info that takes no arguments. 
The function should return a tuple containing the following 
information about a product:

Name: "Laptop"
Price: 999.99
Rating: 4.5
After defining the function, call it and unpack the returned values 
into three variables: product_name, product_price, and product_rating.
Then, print the values of these variables.
"""
def get_product_info():
    Name = "Laptop"
    Price = 999.99
    Rating = 4.5
    return Name, Price, Rating


# call it and unpack the returned values into three variables
product_name, product_price, product_rating = get_product_info()
# print the values of these variables
print(product_name)
print(product_price)
print(product_rating)

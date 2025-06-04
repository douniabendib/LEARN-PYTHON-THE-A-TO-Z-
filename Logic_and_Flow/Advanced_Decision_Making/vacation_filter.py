"""
Write a program that checks if a vacation package meets a customer's
requirements.

Your program should:

Take the following inputs:
destination: The vacation destination (a string)
price: The package price (a float)
nights: Number of nights included (an integer)
family_preference: Whether customer wants family-friendly (a boolean)
package_family_friendly: Whether package is family-friendly (a boolean)
Evaluate if the package is suitable based on these conditions:
Destination must be "Hawaii" or "Bahamas"
Price must be less than $2000
Package must include at least 4 nights
Family-friendliness must match customer's preference
Print the result:
"Package is suitable" if all conditions are met
"Package is not suitable" if any condition is not met
Note: For boolean inputs, enter 1 for True and 0 for False.
"""
destination = input("Enter your vacation destination: ")
price = float(input("Enter the package price: "))
nights = int(input("Enter a number of nights: "))
# 1 for True, 0 for False
family_preference = bool(int(input("Enter if you want family-friendly: ")))
# 1 for True, 0 for False
package_family_friendly = bool(int(input("Enter if package is family-friendly: ")))

# Check if the package is suitable
# Condition 1: Check destination
if (destination == "Hawaii" or destination == "Bahamas"):
    # Condition 2: Check price and nights
    if (price < 2000 and nights >= 4):
        # Condition 3: Check family-friendliness preference
        if (family_preference == package_family_friendly):
            print("Package is suitable")
        else:
            print("Package is not suitable")
    else:
        print("Package is not suitable")
else:
    print("Package is not suitable")

    

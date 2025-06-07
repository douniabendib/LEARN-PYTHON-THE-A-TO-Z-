"""
You're organizing a treasure hunt where participants search for 
treasures in different regions. Each region is represented by a 
set of treasures found there. You need to analyze the data to find:

Shared Treasures: Treasures found in all regions.
Unique Treasures in Region 1: Treasures only found in the first region.
All Treasures: A list of all treasures discovered across all regions.
Exclusive Treasures: Treasures that are unique to one region and not 
shared with any other region.
"""
region1 = eval(input("Enter first region: "))
region2 = eval(input("Enter second region: "))
region3 = eval(input("Enter third region: "))

# 1. Find shared treasures (intersection of all regions)
shared_treasures = region1.intersection(region2, region3)

# 2. Find unique treasures in region1 (difference from other regions)
unique_treasures_region1 = region1.difference(region2, region3)

# 3. Find all treasures (union of all regions)
all_treasures = region1.union(region2, region3)

# 4. Find exclusive treasures (symmetric difference across all regions)
unique_treasures_region2 = region2.difference(region1, region3)
unique_treasures_region3 = region3.difference(region1, region2)
exclusive_treasures = unique_treasures_region1.union(unique_treasures_region2, unique_treasures_region3)

# Print the results
print("Shared treasures:", sorted(list(shared_treasures)))
print("Unique treasures in region1:", sorted(list(unique_treasures_region1)))
print("All treasures:", sorted(list(all_treasures)))
print("Exclusive treasures:", sorted(list(exclusive_treasures)))


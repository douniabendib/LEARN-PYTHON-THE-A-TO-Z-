"""
Create a program that receives a list as input and prints 
four new lists based on the following slicing operations:

**A list containing every fourth element, starting from index 2
**A list containing all elements from the 3rd element to the 3rd 
  to last element.
**A list containing every element in reverse order, skipping 
  every other element
**A list containing the first three and last three elements of 
  the original list. Name the lists list1, list2, list3 
  and list4 - accordingly.
"""
original_list = input("Enter a list: ").split(',')
list1 = original_list[2::4]
list2 = original_list[2:-2]
list3 = original_list[::-2]
list4 = original_list[:3] + original_list[-3:]


print("List 1:", list1)
print("List 2:", list2)
print("List 3:", list3)
print("List 4:", list4)

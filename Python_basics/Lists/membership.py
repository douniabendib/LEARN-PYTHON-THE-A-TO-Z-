"""
Create a function called not_mutual_friends that takes two lists of
 names representing two people's friend lists. The function should 
return a list of names that are friends with only one person
 (not mutual friends).

Let's say we have:

Person A's friends: ["John", "Emma", "Mike", "Sarah"]
Person B's friends: ["Emma", "Tom", "Sarah", "Peter"]
When we call not_mutual_friends with these two lists, 
it should return: ["John", "Mike", "Tom", "Peter"]

Explanation:

"John" and "Mike" are only friends with Person A
"Tom" and "Peter" are only friends with Person B
"Emma" and "Sarah" are mutual friends (friends with both people),
 so they are not included in the result
"""
def not_mutual_friends(list1, list2):
    list3 = list1 + list2
    new_list = []
    for name in list3:
        if name not in list1:
           new_list.append(name)
        elif name not in list2:
           new_list.append(name)
    return new_list


print(not_mutual_friends(["John", "Emma", "Mike", "Sarah"], ["Emma", "Tom", "Sarah", "Peter"]))

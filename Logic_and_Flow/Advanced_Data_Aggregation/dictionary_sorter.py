"""
Create a function named dictionary_sorter that takes a dictionary 
data_dict as an argument. The function should sort the dictionary 
by its values in ascending order and return a new dictionary 
containing the sorted key-value pairs.

For example, if the input dictionary is {'a': 3, 'b': 1, 'c': 2}, 
the function should return a dictionary like this:

{'b': 1, 'c': 2, 'a': 3}
"""
def dictionary_sorter(data_dict):
    sorted_dict = dict(sorted(data_dict.items(), key=lambda item: item[1]))
    return sorted_dict

print(dictionary_sorter({'a': 3, 'b': 1, 'c': 2}))

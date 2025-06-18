"""
Create a function named calculate_lengths that takes a list of words 
words as an argument. The function should use the map() function 
along with a lambda function to calculate the length of each word 
in the list. The function should return a list containing the 
lengths of the words.
"""
def calculate_lengths(words):
    # Use map() with a lambda function to calculate the length of each word
    word_lengths = map(lambda word: len(word), words)
    
    # Return the list of word lengths
    return list(word_lengths)


print(calculate_lengths(["apple","banana","cherry","date","fig"]))

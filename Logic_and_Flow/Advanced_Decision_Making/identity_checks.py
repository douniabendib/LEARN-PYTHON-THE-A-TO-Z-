"""
Create a function named compare_strings that takes two strings,
 str1 and str2, as arguments. The function should perform 
the following operations:

Check if str1 is a substring of str2.
Check if str2 starts with str1.
Check if str2 ends with str1.
Check if str1 and str2 are equal (case-insensitive).
Return a dictionary containing the results of these operations,
with the keys "is_substring","starts_with","ends_with",and "is_equal"
"""
def compare_strings(str1, str2):
    # Check if str1 is a substring of str2
    is_substring = str1 in str2

    # Check if str2 starts with str1
    starts_with = str2.startswith(str1)

    # Check if str2 ends with str1
    ends_with = str2.endswith(str1)

    # Check if str1 and str2 are equal (case-insensitive)
    is_equal = str1.lower() == str2.lower()

    # Return a dictionary containing the results
    return {
        "is_substring": is_substring,
        "starts_with": starts_with,
        "ends_with": ends_with,
        "is_equal": is_equal
    }


print(compare_strings("hello", "hello world"))

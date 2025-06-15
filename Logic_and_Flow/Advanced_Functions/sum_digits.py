"""
Write a recursive function named sum_digits that takes a positive 
integer n as an argument and returns the sum of its digits. 
The function should work as follows:

If n is a single digit (less than 10), return that digit.
Otherwise, return the sum of the last digit of n and the result 
of sum_digits called with n divided by 10 (integer division).
"""
def sum_digits(n):
    if n < 10: # Base Case
        return n
    return (n % 10) + sum_digits(n//10)


print(sum_digits(1))
print(sum_digits(1001))
print(sum_digits(555))

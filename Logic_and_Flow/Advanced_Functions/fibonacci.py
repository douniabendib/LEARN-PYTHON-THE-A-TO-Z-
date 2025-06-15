"""
Write a recursive function named fibonacci that takes a positive 
integer n as an argument and returns the nth Fibonacci number. 
The Fibonacci sequence is defined as:

fibonacci(1) = 0
fibonacci(2) = 1
fibonacci(n) = fibonacci(n-1) + fibonacci(n-2) for n > 2.
"""
def fibonacci(n):
    if n == 1: # Base case
       return 0
    elif n == 2: # Base case
       return 1
    return fibonacci(n - 1) + fibonacci(n - 2) # Recursive step


print(fibonacci(1))
print(fibonacci(2))
print(fibonacci(6))
print(fibonacci(12))
print(fibonacci(21))
print(fibonacci(4)) 

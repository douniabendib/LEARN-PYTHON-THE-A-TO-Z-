"""
Create a function named get_prime_numbers that takes a list 
of integers numbers as an argument. The function should use 
the filter() function along with a lambda function to select 
prime numbers from the list. A prime number is a number greater 
than 1 that has no positive divisors other than 1 and itself. 
The function should return a list containing the selected prime 
numbers.
"""
def get_prime_numbers(numbers):
    def is_prime(n):
        if n <= 1:
            return False
        
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    # Use filter() with a lambda function to select prime numbers
    prime_numbers = filter(lambda x: is_prime(x), numbers)

    # Return the list of selected prime numbers
    return list(prime_numbers)


print(get_prime_numbers([2,3,4,5,10,11,13,17,18,19]))

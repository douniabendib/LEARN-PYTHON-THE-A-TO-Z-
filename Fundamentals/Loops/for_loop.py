"""
Write a program that counts the number of even numbers between 10 and 50 (inclusive).

Use a for loop and an if statement to check if each number is even.

Store the count in a variable called count_even.

Remember, you can check if a number is even by using the modulo operator: number % 2 == 0
"""
count_even = 0
for number in range(10, 51):
    if number % 2 == 0:
        count_even += 1


print(f"count_even = {count_even}")

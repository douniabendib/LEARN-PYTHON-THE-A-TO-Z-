"""
Write a recursive function named print_sequence that takes a positive
integer n as an argument and prints a countdown sequence. For each 
number from n to 1, it should print 'T-minus {number}'. 
When it reaches 0, it should print 'Blast off!'. 
For example, if n is 3, the output should be:

T-minus 3
T-minus 2
T-minus 1
Blast off!
"""
def print_sequence(n):
    if n == 0:
       print("Blast off!")
       return 
    print(f"T-minus {n}")
    print_sequence(n - 1)


print_sequence(5)

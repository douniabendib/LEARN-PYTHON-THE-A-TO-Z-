"""
Write a code that initializes three variables, x, y and z with the values 15, 4, and 23 (respectively).

After that, initialize the following variables:

w that will hold the result of integer division of x by y 
v that will hold the result of integer division of z by x
u that will hold the result of integer division of z by y
Use the // operator for integer division. For example: 7 // 2 equals 3 (not 3.5)
"""
x = 15
y = 4
z = 23
w = x // y
v = z // x
u = z // y

print(f"x = {x}")
print(f"y = {y}")
print(f"z = {z}")
print(f"w = {w}")
print(f"v = {v}")
print(f"u = {u}")

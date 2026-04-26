# Write a program to swap two variables without using a third variable.
# Method 1: Using addition and subtraction
a = True
b = False
print(f"Before swaping : a = {a} b = {b}")
a = a + b 
b = a - b 
a = a - b 
print(f"After swaping : a = {a} b = {b}") 

"""this works because in Python, True is treated as 1 and False is treated as 0 
when used in arithmetic operations. So, the values of a and b are swapped successfully."""



# Method 2: Using bitwise XOR operator
a = 0
b = -4
print(f"Before swaping : a = {a} b = {b}")
a = a ^ b
b = a ^ b 
a = a ^ b
print(f"After swaping : a = {a} b = {b}")

"""this works because the XOR operator has the property that x ^ x = 0 and x ^ 0 = x.
 So, when we perform a = a ^ b, we store the XOR of a and b in a. Then, when we do b = a ^ b,
   we get the original value of a in b. Finally, when we do a = a ^ b, we get the original
     value of b in a."""


# Method 3: Using tuple unpacking
a = 5 
b = 10 
print(f"Before swaping : a = {a} b = {b}")
a, b = b, a
print(f"After swaping : a = {a} b = {b}")

""" this works because Python allows for multiple assignment, which means we can assign
 values to multiple variables in a single line."""

# Method 4: Using multiplication and division
a = 3 
b = 4
if a == 0 or b == 0:
    print("Cannot swap variables using multiplication and division if either variable is zero.")
else:
    print(f"Before swaping : a = {a} b = {b}")
    a = a * b
    b = a // b
    a = a // b
    print(f"After swaping : a = {a} b = {b}")
"""this works because when we multiply a and b, we get the product of the two numbers. 
Then, when we divide the product by b, we get the original value of a. Finally, when we 
divide the product by a, we get the original value of b. However, this method can lead to 
issues if either a or b is zero, as it would result in division by zero."""
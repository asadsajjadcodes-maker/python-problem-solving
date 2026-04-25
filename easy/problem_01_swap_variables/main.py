# Write a program to swap two variables without using a third variable.
# Method 1: Using arithmetic operations
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
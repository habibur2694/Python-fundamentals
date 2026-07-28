#Python Operators

# Arithmetic Operators
x = 10
y = 5
print(x + y)  # Addition
print(x - y)  # Subtraction
print(x * y)  # Multiplication
print(x / y)  # Division
print(x % y)  # Modulus
print(x ** y) # Exponentiation
print(x // y) # Floor Division

# Assignment Operators
x = 10
print(x)  # Same as x = 10
x += 5    # Same as x = x + 5
print(x)  # Output: 15
x -= 5    # Same as x = x - 5
print(x)  # Output: 10
x *= 5    # Same as x = x * 5
print(x)  # Output: 50
x /= 5    # Same as x = x / 5
print(x)  # Output: 10.0

# The Ternary Operator
age = 20
status = "Adult" if age >= 18 else "Not Adult"
print(status)  # Output: Adult

# Comparison Operators
x = 10
y = 5
print(x == y)  # Equal
print(x != y)  # Not Equal
print(x > y)   # Greater Than
print(x < y)   # Less Than
print(x >= y)  # Greater Than or Equal
print(x <= y)  # Less Than or Equal

# Logical Operators
a = True
b = False
print(a and b)  # Output: False
print(a or b)   # Output: True
print(not a)    # Output: False

# Identity Operators
x = 10
y = 10
print(x is y)   # Output: True
print(x is not y)  # Output: False

# Membership Operators
fruits = ["apple", "banana", "cherry"]
print("apple" in fruits)  # Output: True
print("mango" not in fruits)  # Output: True    

# Bitwise Operators
x = 10  # Binary: 1010
y = 4   # Binary: 0100
print(x & y)  # Output: 0 (Binary: 0000)
print(x | y)  # Output: 14 (Binary: 1110)
print(x ^ y)  # Output: 14 (Binary: 1110)
print(~x)     # Output: -11 (Binary: ...1101)
print(x << 1) # Output: 20 (Binary: 10100)
print(x >> 1) # Output: 5 (Binary: 101)

#Operator Precedence


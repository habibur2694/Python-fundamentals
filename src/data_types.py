"""
Text Type:	str
Numeric Types:	int, float, complex
Sequence Types:	list, tuple, range
Mapping Type:	dict
Set Types:	set, frozenset
Boolean Type:	bool
Binary Types:	bytes, bytearray, memoryview
None Type:	NoneType
"""

"""
=========================================
Python Fundamentals - Data Types
Author : Habu Lab
Topic  : Python Data Types
=========================================

This file covers:
1. String
2. Integer
3. Float
4. Complex
5. Boolean
6. List
7. Tuple
8. Set
9. Dictionary
10. Range
11. Bytes
12. Bytearray
13. Memoryview
14. NoneType
15. Type Checking
16. Type Casting
17. Mutable vs Immutable
"""

print("=" * 60)
print("           PYTHON DATA TYPES")
print("=" * 60)

# =========================================
# 1. STRING
# =========================================

print("\n1. STRING (str)")
language = "Python"
print("Value :", language)
print("Type  :", type(language))

# =========================================
# 2. INTEGER
# =========================================

print("\n2. INTEGER (int)")
age = 23
print("Value :", age)
print("Type  :", type(age))

# =========================================
# 3. FLOAT
# =========================================

print("\n3. FLOAT (float)")
cgpa = 3.95
print("Value :", cgpa)
print("Type  :", type(cgpa))

# =========================================
# 4. COMPLEX
# =========================================

print("\n4. COMPLEX (complex)")
number = 5 + 2j
print("Value :", number)
print("Type  :", type(number))

# =========================================
# 5. BOOLEAN
# =========================================

print("\n5. BOOLEAN (bool)")
is_student = True
print("Value :", is_student)
print("Type  :", type(is_student))

# =========================================
# 6. LIST
# =========================================

print("\n6. LIST")
fruits = ["Apple", "Banana", "Orange"]
print("Value :", fruits)
print("Type  :", type(fruits))

# List is Mutable
fruits.append("Mango")
print("After Append :", fruits)

# =========================================
# 7. TUPLE
# =========================================

print("\n7. TUPLE")
numbers = (10, 20, 30)
print("Value :", numbers)
print("Type  :", type(numbers))

# =========================================
# 8. SET
# =========================================

print("\n8. SET")
colors = {"Red", "Green", "Blue", "Red"}
print("Value :", colors)
print("Type  :", type(colors))

# =========================================
# 9. DICTIONARY
# =========================================

print("\n9. DICTIONARY")

student = {
    "Name": "Habibur",
    "Age": 23,
    "Department": "CSE",
    "CGPA": 3.95
}

print("Value :", student)
print("Type  :", type(student))

# =========================================
# 10. RANGE
# =========================================

print("\n10. RANGE")
numbers = range(1, 6)
print(list(numbers))
print(type(numbers))

# =========================================
# 11. BYTES
# =========================================

print("\n11. BYTES")

data = b"Python"
print(data)
print(type(data))

# =========================================
# 12. BYTEARRAY
# =========================================

print("\n12. BYTEARRAY")

data = bytearray(5)
print(data)
print(type(data))

# =========================================
# 13. MEMORYVIEW
# =========================================

print("\n13. MEMORYVIEW")

memory = memoryview(bytes(5))
print(memory)
print(type(memory))

# =========================================
# 14. NONETYPE
# =========================================

print("\n14. NONETYPE")

value = None
print(value)
print(type(value))

# =========================================
# TYPE CHECKING
# =========================================

print("\n" + "=" * 60)
print("TYPE CHECKING")
print("=" * 60)

x = 100
y = 20.5
z = "Python"

print(type(x))
print(type(y))
print(type(z))

# =========================================
# TYPE CASTING
# =========================================

print("\n" + "=" * 60)
print("TYPE CASTING")
print("=" * 60)

number = "100"

print(number)
print(type(number))

number = int(number)

print(number)
print(type(number))

price = 99

print(float(price))
print(str(price))

# =========================================
# MEMORY ADDRESS
# =========================================

print("\n" + "=" * 60)
print("MEMORY ADDRESS")
print("=" * 60)

name = "Python"

print(name)
print(id(name))

# =========================================
# MUTABLE VS IMMUTABLE
# =========================================

print("\n" + "=" * 60)
print("MUTABLE VS IMMUTABLE")
print("=" * 60)

my_list = [1, 2, 3]
my_list.append(4)

print("Mutable List :", my_list)

my_tuple = (1, 2, 3)

print("Immutable Tuple :", my_tuple)

# =========================================
# REAL LIFE EXAMPLE
# =========================================

print("\n" + "=" * 60)
print("REAL LIFE EXAMPLE")
print("=" * 60)

student = {
    "Name": "Habibur",
    "Age": 23,
    "Department": "Computer Science",
    "CGPA": 3.92,
    "Graduated": False,
    "Skills": ["Python", "SQL", "Git"]
}

for key, value in student.items():
    print(f"{key:12}: {value}")

# =========================================
# SUMMARY
# =========================================

print("\n" + "=" * 60)
print("SUMMARY")
print("=" * 60)

print("""
str         -> Text
int         -> Integer Number
float       -> Decimal Number
complex     -> Complex Number
bool        -> True / False
list        -> Ordered & Mutable
tuple       -> Ordered & Immutable
set         -> Unique Values
dict        -> Key-Value Pair
range       -> Sequence
bytes       -> Immutable Binary Data
bytearray   -> Mutable Binary Data
memoryview  -> Memory Object
NoneType    -> No Value
""")

print("=" * 60)
print("End of Python Data Types Program")
print("=" * 60)
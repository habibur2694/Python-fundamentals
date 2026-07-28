# ==========================================
# Python Input & Output (I/O) Complete Note
# ==========================================


# ------------------------------------------
# 1. Basic Output using print()
# ------------------------------------------

print("Hello Python")
print("Welcome to Python Programming")


# ------------------------------------------
# 2. Printing Variables
# ------------------------------------------

name = "Habib"
age = 25

print(name)
print(age)


# ------------------------------------------
# 3. Multiple Values Print
# ------------------------------------------

print("Name:", name, "Age:", age)


# ------------------------------------------
# 4. String Formatting (f-string)
# ------------------------------------------

print(f"My name is {name} and my age is {age}")


# ------------------------------------------
# 5. Basic Input
# ------------------------------------------

# name = input("Enter your name: ")
# print(name)



# ------------------------------------------
# 6. Integer Input
# ------------------------------------------

# age = int(input("Enter your age: "))
# print(age)



# ------------------------------------------
# 7. Float Input
# ------------------------------------------

# height = float(input("Enter your height: "))
# print(height)



# ------------------------------------------
# 8. Multiple Input using split()
# ------------------------------------------

# name, city = input("Enter name and city: ").split()

# print(name)
# print(city)



# ------------------------------------------
# 9. Multiple Number Input using map()
# ------------------------------------------

# a, b = map(int, input("Enter two numbers: ").split())

# print(a + b)



# ------------------------------------------
# 10. Type Checking
# ------------------------------------------

number = 100

print(type(number))


text = "Python"

print(type(text))


# ------------------------------------------
# 11. Escape Character
# ------------------------------------------

print("Python\nProgramming")


print("Python\tProgramming")



# ------------------------------------------
# 12. Separator (sep)
# ------------------------------------------

print("Python", "Java", "C++", sep=" | ")



# ------------------------------------------
# 13. End Parameter
# ------------------------------------------

print("Hello", end=" ")
print("Python")



# ==========================================
# Practical Examples
# ==========================================



# ------------------------------------------
# Example 1: Student Information System
# ------------------------------------------

# student_name = input("Enter student name: ")
# student_age = int(input("Enter age: "))
# student_gpa = float(input("Enter GPA: "))


# print("\n----- Student Information -----")

# print(f"Name : {student_name}")
# print(f"Age  : {student_age}")
# print(f"GPA  : {student_gpa}")




# ------------------------------------------
# Example 2: Addition Program
# ------------------------------------------

# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))


# result = num1 + num2


# print("Total =", result)




# ------------------------------------------
# Example 3: Simple Calculator
# ------------------------------------------

# num1 = float(input("Enter first number: "))
# operator = input("Enter operator (+,-,*,/): ")
# num2 = float(input("Enter second number: "))


# if operator == "+":
#     print(num1 + num2)

# elif operator == "-":
#     print(num1 - num2)

# elif operator == "*":
#     print(num1 * num2)

# elif operator == "/":
#     print(num1 / num2)

# else:
#     print("Invalid Operator")




# ------------------------------------------
# Example 4: Login System
# ------------------------------------------

# username = input("Enter username: ")
# password = input("Enter password: ")


# if username == "admin" and password == "1234":

#     print("Login Successful")

# else:

#     print("Invalid Username or Password")



# ==========================================
# End of Python Input Output Note
# ==========================================
# ==========================================
# Python Conditions (if, elif, else)
# Complete Note + Code
# ==========================================


# ------------------------------------------
# 1. What is Condition?
# ------------------------------------------

# Condition ব্যবহার করে Python program সিদ্ধান্ত নেয়।
# Condition True হলে code execute হবে।
# False হলে অন্য code execute হবে।



# ------------------------------------------
# 2. Comparison Operators
# ------------------------------------------

# ==  Equal
# !=  Not Equal
# >   Greater than
# <   Less than
# >=  Greater than or Equal
# <=  Less than or Equal


a = 10
b = 20

print(a == b)
print(a != b)
print(a < b)



# ------------------------------------------
# 3. Simple if Statement
# ------------------------------------------

age = 18

if age >= 18:
    print("You can vote")



# ------------------------------------------
# 4. if - else Statement
# ------------------------------------------

age = 15

if age >= 18:
    print("You can vote")

else:
    print("You cannot vote")



# ------------------------------------------
# 5. if - elif - else
# ------------------------------------------

marks = 85


if marks >= 90:

    print("Grade A+")

elif marks >= 80:

    print("Grade A")

elif marks >= 70:

    print("Grade B")

elif marks >= 60:

    print("Grade C")

else:

    print("Fail")



# ------------------------------------------
# 6. Nested if Condition
# ------------------------------------------

username = "admin"
password = "1234"


if username == "admin":

    if password == "1234":

        print("Login Successful")

    else:

        print("Wrong Password")

else:

    print("Wrong Username")



# ------------------------------------------
# 7. Logical Operators
# ------------------------------------------

# and
# or
# not


age = 25
country = "Bangladesh"


if age >= 18 and country == "Bangladesh":

    print("Eligible")



# OR Example

day = "Friday"


if day == "Friday" or day == "Saturday":

    print("Weekend")



# NOT Example

is_raining = False


if not is_raining:

    print("Go Outside")



# ------------------------------------------
# 8. Membership Condition
# ------------------------------------------

# in
# not in


name = "Python"


if "P" in name:

    print("P exists")



# ------------------------------------------
# 9. User Input Condition Example
# ------------------------------------------

# age = int(input("Enter your age: "))


# if age >= 18:

#     print("Adult")

# else:

#     print("Minor")




# ------------------------------------------
# 10. Even Odd Number Check
# ------------------------------------------

number = 10


if number % 2 == 0:

    print("Even Number")

else:

    print("Odd Number")



# ------------------------------------------
# 11. Positive Negative Zero Check
# ------------------------------------------

number = -5


if number > 0:

    print("Positive")

elif number < 0:

    print("Negative")

else:

    print("Zero")



# ------------------------------------------
# 12. Simple Calculator Using Condition
# ------------------------------------------

num1 = 20
num2 = 10
operator = "+"


if operator == "+":

    print(num1 + num2)

elif operator == "-":

    print(num1 - num2)

elif operator == "*":

    print(num1 * num2)

elif operator == "/":

    print(num1 / num2)

else:

    print("Invalid Operator")



# ------------------------------------------
# 13. Login System Project
# ------------------------------------------

user = "habib"
password = "python123"


if user == "habib" and password == "python123":

    print("Welcome Habib")

else:

    print("Login Failed")



# ------------------------------------------
# 14. Student Result System
# ------------------------------------------

marks = 75


if marks >= 80:

    result = "A"

elif marks >= 70:

    result = "B"

elif marks >= 60:

    result = "C"

elif marks >= 40:

    result = "D"

else:

    result = "Fail"


print("Result:", result)



# ==========================================
# Important Shortcut
# ==========================================

# if       = যদি
# elif     = না হলে যদি
# else     = না হলে


# Condition Structure:

"""
if condition:

    code

elif condition:

    code

else:

    code
"""


# ==========================================
# End of Python Conditions
# ==========================================
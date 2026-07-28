# ==========================================
# Python Functions Complete Note + Code
# ==========================================


# ==========================================
# What is Function?
# ==========================================

# Function হলো এমন একটি code block
# যেটা একটি নির্দিষ্ট কাজ করার জন্য তৈরি করা হয়।
#
# Function ব্যবহার করলে:
# 1. Code reuse করা যায়
# 2. Code clean থাকে
# 3. Debug করা সহজ হয়



# ==========================================
# 1. Creating a Function
# ==========================================


def hello():

    print("Hello Python")


# Calling Function

hello()



# ==========================================
# 2. Function with Parameters
# ==========================================


def greet(name):

    print("Hello", name)


greet("Habib")
greet("Rahim")



# ==========================================
# 3. Multiple Parameters
# ==========================================


def add(a, b):

    print(a + b)


add(10, 20)



# ==========================================
# 4. Function with Return Value
# ==========================================


def multiply(a, b):

    result = a * b

    return result



answer = multiply(5, 4)

print(answer)



# ==========================================
# 5. Default Parameter
# ==========================================


def country(name="Bangladesh"):

    print(name)



country()

country("Japan")



# ==========================================
# 6. Keyword Arguments
# ==========================================


def student(name, age):

    print("Name:", name)
    print("Age:", age)



student(
    age=25,
    name="Habib"
)



# ==========================================
# 7. Arbitrary Arguments (*args)
# ==========================================


# যখন parameter সংখ্যা জানা থাকে না


def total(*numbers):

    sum = 0

    for number in numbers:

        sum += number

    return sum



print(total(10,20,30))

print(total(5,10,15,20))



# ==========================================
# 8. Keyword Arbitrary Arguments (**kwargs)
# ==========================================


def information(**data):

    for key,value in data.items():

        print(key, ":", value)



information(
    name="Habib",
    age=25,
    skill="Python"
)



# ==========================================
# 9. Local Variable
# ==========================================


def test():

    x = 10

    print(x)



test()



# ==========================================
# 10. Global Variable
# ==========================================


x = 100


def show():

    print(x)



show()



# ==========================================
# 11. Lambda Function
# ==========================================


# ছোট function এক লাইনে লেখার জন্য


square = lambda x: x * x


print(square(5))



# ==========================================
# 12. Function with Condition
# ==========================================


def check_age(age):

    if age >= 18:

        return "Adult"

    else:

        return "Minor"



print(check_age(20))

print(check_age(15))



# ==========================================
# 13. Function with Loop
# ==========================================


def print_numbers(n):

    for i in range(1,n+1):

        print(i)



print_numbers(5)



# ==========================================
# 14. Calculator Function
# ==========================================


def calculator(a,b,operator):


    if operator == "+":

        return a+b


    elif operator == "-":

        return a-b


    elif operator == "*":

        return a*b


    elif operator == "/":

        return a/b


    else:

        return "Invalid Operator"



print(calculator(10,5,"+"))

print(calculator(10,5,"*"))



# ==========================================
# 15. Student Result Function
# ==========================================


def grade(marks):

    if marks >= 80:

        return "A"


    elif marks >= 70:

        return "B"


    elif marks >= 60:

        return "C"


    else:

        return "Fail"



print(grade(85))

print(grade(50))



# ==========================================
# 16. Real Project Example
# Login Function
# ==========================================


def login(username,password):

    if username == "admin" and password == "1234":

        return "Login Successful"

    else:

        return "Login Failed"



print(login("admin","1234"))

print(login("user","1111"))



# ==========================================
# Function Summary
# ==========================================


# def
# -> Function তৈরি করার keyword


# parameter
# -> Function এর input


# argument
# -> Function call করার সময় value


# return
# -> Function থেকে value ফেরত দেয়


# *args
# -> Multiple arguments


# **kwargs
# -> Multiple keyword arguments


# lambda
# -> One line function



# ==========================================
# Function Structure
# ==========================================

"""
def function_name(parameters):

    code

    return value
"""


# ==========================================
# End of Python Functions
# ==========================================
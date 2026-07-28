# ==========================================
# Python Modules Complete Note + Code
# ==========================================


# ==========================================
# What is Module?
# ==========================================

# Module হলো একটি Python file (.py)
# যেখানে variables, functions, classes এবং code লেখা থাকে।
#
# অন্য file এ সেই code reuse করার জন্য Module ব্যবহার করা হয়।
#
# Advantages:
# 1. Code reuse করা যায়
# 2. Project organize করা যায়
# 3. Code maintain করা সহজ হয়



# ==========================================
# Types of Modules
# ==========================================

# Python এ দুই ধরনের Module আছে:

# 1. Built-in Module
#    -> Python এর সাথে আগে থেকেই থাকে

# Example:
# math, random, datetime, os


# 2. User Defined Module
#    -> Programmer নিজে তৈরি করে



# ==========================================
# 1. Import Module
# ==========================================


import math


print(math.sqrt(25))

print(math.pi)



# ==========================================
# 2. Import Specific Function
# ==========================================


from math import sqrt


print(sqrt(64))



# ==========================================
# 3. Import Multiple Functions
# ==========================================


from math import sqrt, factorial


print(sqrt(81))

print(factorial(5))



# ==========================================
# 4. Module Alias (as)
# ==========================================


import math as m


print(m.sqrt(100))

print(m.pi)



# ==========================================
# 5. Built-in Module Examples
# ==========================================



# ------------------------------------------
# Math Module
# ------------------------------------------


import math


number = 16


print("Square Root:", math.sqrt(number))

print("Power:", math.pow(2,3))

print("Ceil:", math.ceil(4.2))

print("Floor:", math.floor(4.8))



# ------------------------------------------
# Random Module
# ------------------------------------------


import random


print(random.randint(1,10))


names = [
    "Habib",
    "Rahim",
    "Karim"
]


print(random.choice(names))



# ------------------------------------------
# DateTime Module
# ------------------------------------------


import datetime


today = datetime.datetime.now()


print(today)

print(today.year)

print(today.month)

print(today.day)



# ------------------------------------------
# OS Module
# ------------------------------------------


import os


print(os.getcwd())



# ==========================================
# User Defined Module
# ==========================================


# দুইটি file তৈরি করতে হবে:


# calculator.py

"""
def add(a,b):

    return a+b


def subtract(a,b):

    return a-b
"""


# main.py

"""
import calculator


print(calculator.add(10,20))

print(calculator.subtract(20,5))
"""



# ==========================================
# Import All (*)
# ==========================================


# সব function import করার জন্য


# from math import *



# ==========================================
# Module Search Path
# ==========================================


import sys


print(sys.path)



# ==========================================
# Creating Custom Module Example
# ==========================================


# File: student.py

"""
name = "Habib"


def info():

    print("Python Student")
"""



# File: main.py

"""
import student


print(student.name)

student.info()
"""



# ==========================================
# Package vs Module
# ==========================================


# Module:
# একটি Python file (.py)


# Package:
# একাধিক Module এর collection



# Example:

"""
project/

    main.py

    package/

        math.py

        student.py

"""



# ==========================================
# Real Project Example
# ==========================================


# Project Structure:


"""
Finance_App/

    main.py

    database.py

    calculator.py

    user.py

"""



# main.py

"""
import calculator
import database
import user
"""



# ==========================================
# Common Python Built-in Modules
# ==========================================


"""
math       -> Mathematical operations

random     -> Random values

datetime   -> Date and time

os         -> Operating system tasks

sys        -> Python system information

json       -> JSON data handling

csv        -> CSV file handling

re         -> Regular expression

statistics -> Statistics calculation

"""



# ==========================================
# Practice Example
# Random Password Generator
# ==========================================


import random
import string


characters = string.ascii_letters + string.digits


password = ""


for i in range(8):

    password += random.choice(characters)


print("Password:", password)



# ==========================================
# Module Summary
# ==========================================


# import
# -> Module load করার জন্য


# from import
# -> Specific function নেওয়ার জন্য


# as
# -> Short name দেওয়ার জন্য


# Built-in Module
# -> Python এর সাথে আসে


# User Defined Module
# -> নিজের তৈরি Module



# ==========================================
# End of Python Modules
# ==========================================
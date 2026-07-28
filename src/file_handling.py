# ==========================================
# Python Exceptions & File Handling
# Complete Note + Code
# ==========================================



# ==========================================
# PART 1: Exception Handling
# ==========================================


# ==========================================
# What is Exception?
# ==========================================

# Exception হলো program চলার সময়
# যে error তৈরি হয়।
#
# Exception Handling ব্যবহার করে
# program crash হওয়া থেকে রক্ষা করা হয়।



# Common Errors:

# ZeroDivisionError
# ValueError
# TypeError
# FileNotFoundError
# IndexError



# ==========================================
# 1. Basic try-except
# ==========================================


try:

    number = 10 / 0

    print(number)


except:

    print("Something went wrong")



# ==========================================
# 2. Specific Exception Handling
# ==========================================


try:

    number = int(input("Enter number: "))

    print(100 / number)


except ZeroDivisionError:

    print("Cannot divide by zero")


except ValueError:

    print("Please enter a number")



# ==========================================
# 3. Multiple Exception
# ==========================================


try:

    a = int(input("Enter A: "))

    b = int(input("Enter B: "))

    print(a / b)



except (ValueError, ZeroDivisionError):

    print("Invalid Input")



# ==========================================
# 4. else Block
# ==========================================


try:

    x = 10

    y = 2

    result = x / y


except ZeroDivisionError:

    print("Error")


else:

    print("Result:", result)



# ==========================================
# 5. finally Block
# ==========================================


try:

    print("Try Block")


except:

    print("Error")


finally:

    print("Always Execute")



# ==========================================
# 6. Raise Exception
# ==========================================


age = -5


if age < 0:

    raise ValueError("Age cannot be negative")



# ==========================================
# Custom Exception
# ==========================================


class AgeError(Exception):

    pass



age = 10


if age < 18:

    raise AgeError("You are not eligible")



# ==========================================
# PART 2: File Handling
# ==========================================



# ==========================================
# What is File Handling?
# ==========================================

# File Handling ব্যবহার করে
# Python দিয়ে file create,
# read, write এবং update করা যায়.



# File Modes:

# r  -> Read
# w  -> Write
# a  -> Append
# x  -> Create



# ==========================================
# 1. Create and Write File
# ==========================================


file = open(
    "student.txt",
    "w"
)


file.write(
    "Name: Habib\n"
)

file.write(
    "Skill: Python"
)


file.close()



# ==========================================
# 2. Read File
# ==========================================


file = open(
    "student.txt",
    "r"
)


data = file.read()


print(data)


file.close()



# ==========================================
# 3. Read Line
# ==========================================


file = open(
    "student.txt",
    "r"
)


line = file.readline()


print(line)


file.close()



# ==========================================
# 4. Read All Lines
# ==========================================


file = open(
    "student.txt",
    "r"
)


lines = file.readlines()


print(lines)


file.close()



# ==========================================
# 5. Append Data
# ==========================================


file = open(
    "student.txt",
    "a"
)


file.write(
    "\nCourse: Machine Learning"
)


file.close()



# ==========================================
# 6. Using with Statement
# ==========================================


# Best practice
# Automatically file close করে।


with open(
    "student.txt",
    "r"
) as file:


    content = file.read()


    print(content)



# ==========================================
# 7. Check File Exists
# ==========================================


import os


if os.path.exists("student.txt"):

    print("File Exists")


else:

    print("File Not Found")



# ==========================================
# 8. Delete File
# ==========================================


# import os

# os.remove("student.txt")



# ==========================================
# 9. Write User Data into File
# ==========================================


name = "Habib"

age = 25


with open(
    "user.txt",
    "w"
) as file:


    file.write(
        f"Name: {name}\n"
    )

    file.write(
        f"Age: {age}"
    )



# ==========================================
# 10. Exception + File Handling
# ==========================================


try:


    with open(
        "data.txt",
        "r"
    ) as file:


        print(file.read())



except FileNotFoundError:


    print("File does not exist")



# ==========================================
# 11. CSV File Handling
# ==========================================


import csv



# Write CSV

with open(
    "students.csv",
    "w",
    newline=""
) as file:


    writer = csv.writer(file)


    writer.writerow(
        [
            "Name",
            "Age",
            "Skill"
        ]
    )


    writer.writerow(
        [
            "Habib",
            25,
            "Python"
        ]
    )



# Read CSV


with open(
    "students.csv",
    "r"
) as file:


    reader = csv.reader(file)


    for row in reader:

        print(row)



# ==========================================
# 12. JSON File Handling
# ==========================================


import json



student = {

    "name":"Habib",

    "age":25,

    "skill":"Python"

}



# Write JSON


with open(
    "student.json",
    "w"
) as file:


    json.dump(
        student,
        file,
        indent=4
    )



# Read JSON


with open(
    "student.json",
    "r"
) as file:


    data = json.load(file)


    print(data)



# ==========================================
# Real Project Example
# Simple Notes App
# ==========================================


def save_note(note):


    with open(
        "notes.txt",
        "a"
    ) as file:


        file.write(
            note + "\n"
        )



def read_notes():


    try:


        with open(
            "notes.txt",
            "r"
        ) as file:


            print(
                file.read()
            )


    except FileNotFoundError:


        print(
            "No notes found"
        )



save_note("Learn Python File Handling")


read_notes()



# ==========================================
# Summary
# ==========================================


# Exception Handling:

# try
# -> Risky code


# except
# -> Error handle


# else
# -> Error না হলে run


# finally
# -> Always run



# File Handling:

# open()
# -> File open


# read()
# -> File read


# write()
# -> File write


# close()
# -> File close


# with open()
# -> Best practice



# ==========================================
# End of Exception & File Handling
# ==========================================
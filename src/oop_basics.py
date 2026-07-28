# ==========================================
# Python OOP Basics Complete Note + Code
# ==========================================


# ==========================================
# What is OOP?
# ==========================================

# OOP = Object Oriented Programming
#
# Programming এর এমন একটি method যেখানে
# data (variables) এবং functions কে একসাথে
# Object হিসেবে ব্যবহার করা হয়।
#
# Real world object কে programming এ represent
# করার জন্য OOP ব্যবহার করা হয়.


# Example:
#
# Real World:
# Car
#
# Properties:
# color, model, speed
#
# Actions:
# drive(), stop()



# ==========================================
# Main Concepts of OOP
# ==========================================


# 1. Class
# 2. Object
# 3. Constructor
# 4. Instance Variable
# 5. Instance Method
# 6. Encapsulation
# 7. Inheritance
# 8. Polymorphism



# ==========================================
# 1. Class
# ==========================================


# Class হলো Object তৈরি করার blueprint


class Student:

    name = "Habib"
    age = 25


print(Student.name)
print(Student.age)



# ==========================================
# 2. Object
# ==========================================


# Object হলো Class এর instance


class Student:

    name = "Habib"


student1 = Student()


print(student1.name)



# ==========================================
# 3. Constructor (__init__)
# ==========================================


# Constructor automatically call হয়
# যখন Object তৈরি করা হয়।


class Student:


    def __init__(self, name, age):

        self.name = name
        self.age = age



student1 = Student("Habib", 25)


print(student1.name)
print(student1.age)



# ==========================================
# 4. self Keyword
# ==========================================


# self বর্তমান object কে represent করে।


class Person:


    def __init__(self, name):

        self.name = name



    def show(self):

        print("Name:", self.name)



person1 = Person("Rahim")


person1.show()



# ==========================================
# 5. Instance Variable
# ==========================================


class Car:


    def __init__(self, brand, color):

        self.brand = brand
        self.color = color



car1 = Car("Toyota", "Black")


print(car1.brand)
print(car1.color)



# ==========================================
# 6. Instance Method
# ==========================================


class Mobile:


    def __init__(self, brand):

        self.brand = brand



    def display(self):

        print("Mobile Brand:", self.brand)



phone = Mobile("Samsung")


phone.display()



# ==========================================
# 7. Multiple Objects
# ==========================================


class Employee:


    def __init__(self, name, salary):

        self.name = name
        self.salary = salary



employee1 = Employee("Habib", 50000)

employee2 = Employee("Karim", 60000)


print(employee1.name)
print(employee2.name)



# ==========================================
# 8. Class Variable
# ==========================================


class Company:


    company_name = "Google"



    def __init__(self, employee):

        self.employee = employee



emp1 = Company("John")


print(emp1.employee)

print(emp1.company_name)



# ==========================================
# 9. Encapsulation
# ==========================================


# Data hide করার process


class BankAccount:


    def __init__(self, balance):

        self.__balance = balance



    def get_balance(self):

        return self.__balance



account = BankAccount(1000)


print(account.get_balance())



# ==========================================
# 10. Inheritance
# ==========================================


# একটি Class অন্য Class এর
# properties এবং methods ব্যবহার করতে পারে।



class Animal:


    def sound(self):

        print("Animal makes sound")



class Dog(Animal):

    def bark(self):

        print("Dog barks")



dog = Dog()


dog.sound()

dog.bark()



# ==========================================
# 11. Types of Inheritance
# ==========================================


# Single Inheritance
# Multiple Inheritance
# Multilevel Inheritance
# Hierarchical Inheritance



# ==========================================
# 12. Polymorphism
# ==========================================


# একই method নাম কিন্তু
# different behavior



class Cat:


    def sound(self):

        print("Meow")



class Dog:


    def sound(self):

        print("Bark")



cat = Cat()

dog = Dog()


cat.sound()

dog.sound()



# ==========================================
# 13. Class Method
# ==========================================


class Student:


    school = "ABC School"



    @classmethod
    def show_school(cls):

        print(cls.school)



Student.show_school()



# ==========================================
# 14. Static Method
# ==========================================


class Calculator:


    @staticmethod
    def add(a,b):

        return a+b



print(Calculator.add(10,20))



# ==========================================
# Real Project Example
# User Management System
# ==========================================


class User:


    def __init__(self, username, email):

        self.username = username
        self.email = email



    def profile(self):

        print("Username:", self.username)

        print("Email:", self.email)




user1 = User(
    "habib123",
    "habib@gmail.com"
)


user1.profile()



# ==========================================
# OOP Structure
# ==========================================


"""
class ClassName:

    def __init__(self, parameters):

        self.variable = value


    def method(self):

        code



object_name = ClassName(arguments)

"""



# ==========================================
# OOP Summary
# ==========================================


# Class
# -> Object তৈরির blueprint


# Object
# -> Class এর instance


# __init__
# -> Constructor


# self
# -> Current object


# Encapsulation
# -> Data hiding


# Inheritance
# -> Code reuse


# Polymorphism
# -> Same method different behavior



# ==========================================
# End of Python OOP Basics
# ==========================================
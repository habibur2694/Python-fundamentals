# ==========================================
# Python Loops Complete Note + Code
# ==========================================


# ==========================================
# What is Loop?
# ==========================================

# Loop ব্যবহার করে একই কাজ বারবার করা যায়।
# যখন একই code multiple times execute করতে হয়,
# তখন Loop ব্যবহার করা হয়।


# Python এ দুই ধরনের Loop আছে:

# 1. for Loop
# 2. while Loop



# ==========================================
# 1. for Loop
# ==========================================

# for loop sequence এর প্রতিটি item নিয়ে কাজ করে।


# Example 1: Print numbers

for i in range(5):

    print(i)



# Output:
# 0
# 1
# 2
# 3
# 4



# ==========================================
# range() Function
# ==========================================


# range(start, stop, step)


# Example:

for i in range(1, 6):

    print(i)


# Output:
# 1
# 2
# 3
# 4
# 5



# ==========================================
# Step ব্যবহার
# ==========================================


for i in range(0, 10, 2):

    print(i)


# Output:
# 0
# 2
# 4
# 6
# 8



# ==========================================
# Loop with String
# ==========================================


name = "Python"


for letter in name:

    print(letter)



# ==========================================
# Loop with List
# ==========================================


students = [
    "Habib",
    "Rahim",
    "Karim"
]


for student in students:

    print(student)



# ==========================================
# Loop with Tuple
# ==========================================


numbers = (10,20,30,40)


for number in numbers:

    print(number)



# ==========================================
# Loop with Dictionary
# ==========================================


student = {

    "name":"Habib",
    "age":25,
    "skill":"Python"

}


for key in student:

    print(key)



# Value print

for value in student.values():

    print(value)



# Key and Value

for key,value in student.items():

    print(key, value)




# ==========================================
# 2. while Loop
# ==========================================


# while condition True থাকা পর্যন্ত loop চলবে।


count = 1


while count <= 5:

    print(count)

    count += 1



# Output:

# 1
# 2
# 3
# 4
# 5



# ==========================================
# User Input with while Loop
# ==========================================


# password = ""


# while password != "1234":

#     password = input("Enter password: ")


# print("Login Successful")




# ==========================================
# break Statement
# ==========================================


# Loop বন্ধ করার জন্য break ব্যবহার হয়।


for i in range(1,10):

    if i == 5:

        break

    print(i)



# Output:

# 1
# 2
# 3
# 4



# ==========================================
# continue Statement
# ==========================================


# Current iteration skip করে next iteration এ যায়।


for i in range(1,6):

    if i == 3:

        continue

    print(i)



# Output:

# 1
# 2
# 4
# 5



# ==========================================
# Nested Loop
# ==========================================


for i in range(1,4):

    for j in range(1,4):

        print(i,j)



# ==========================================
# Multiplication Table
# ==========================================


number = 5


for i in range(1,11):

    print(number, "x", i, "=", number*i)




# ==========================================
# Sum of Numbers
# ==========================================


total = 0


for i in range(1,11):

    total = total + i


print("Total =", total)



# ==========================================
# Even Number Print
# ==========================================


for i in range(1,20):

    if i % 2 == 0:

        print(i)



# ==========================================
# Odd Number Print
# ==========================================


for i in range(1,20):

    if i % 2 != 0:

        print(i)




# ==========================================
# Simple ATM Example using while Loop
# ==========================================


balance = 1000


while True:

    print("\n1. Check Balance")
    print("2. Withdraw")
    print("3. Exit")


    choice = int(input("Choose option: "))


    if choice == 1:

        print("Balance:", balance)


    elif choice == 2:

        amount = int(input("Enter amount: "))

        if amount <= balance:

            balance -= amount

            print("Withdraw Successful")

        else:

            print("Insufficient Balance")


    elif choice == 3:

        print("Thank You")

        break


    else:

        print("Invalid Choice")



# ==========================================
# Loop Shortcut Summary
# ==========================================


# for loop
# -> যখন কয়বার চলবে জানা থাকে


# while loop
# -> যতক্ষণ condition True থাকবে


# break
# -> Loop বন্ধ করে


# continue
# -> Current step skip করে



# ==========================================
# End of Python Loops
# ==========================================
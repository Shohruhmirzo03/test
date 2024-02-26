
# users = []
# def add_user(id, name, lastname, age, address, email, phone):
#     users.extend([id, name, lastname, age, address, email, phone])
#     return users
#
#
# while True:
#     id =  input("ID: ")
#     name = input("Name: ")
#     last_name = input("Lastname: ")
#     age = int(input("Age: "))
#     address = input("Address: ")
#     email = input("Email: ")
#     phone = input("Phone: ")
#     command = input("Yana ma'lumot qo'shasizmi: ")
#     if command == 'stop':
#         print(add_user(id, name, last_name, age, address, email, phone))
#         break



#-----------------------------------------------------------------------------------------------------------------



# users = []
# def add_user(id, name, lastname, age, address, email, phone):
#     users.extend([id, name, lastname, age, address, email, phone])
#     return users
#
#
# while True:
#     id =  input("ID: ")
#     name = input("Name: ")
#     last_name = input("Lastname: ")
#     age = int(input("Age: "))
#     address = input("Address: ")
#     email = input("Email: ")
#     phone = input("Phone: ")
#     command = input("Yana ma'lumot qo'shasizmi: ")
#     print(tuple(add_user(name, last_name, age, address, email, phone)))
#     if command == 'stop':
#         print(add_user(id, name, last_name, age, address, email, phone))
#         break

#------------------------------------------------------------------------------------------------------------------

import csv

with open("user_info.csv", mode="w") as file:
    writer = csv.writer(file, delimiter="|", lineterminator="\n")
    writer.writerow(
        ["ID", "NAME", "LAST NAME", "AGE", "ADDRESS", "EMAIL", "PHONE"]


    )
# users = [
#     [1, "Toxir", "Toxirov", 20, "Fergana", "toxir@gmail.com", 901234455]
# ]
for user in users:
    print(user)
    with open("user_info.csv", mode="a") as file:
        writer = csv.writer(file, delimiter="|", lineterminator="\n")
        writer.writerow(
            user
        )


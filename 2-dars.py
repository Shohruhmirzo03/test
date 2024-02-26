

# from decimal import Decimal
#
# print(Decimal('0.1')+Decimal('0.1')+Decimal('0.1') == Decimal('0.3'))
#
# print(Decimal('0.1')+Decimal('0.1')+Decimal('0.1'))


# def users(id, name, lastname, age, address):
#     users = [id, name, lastname, age, address]
#     return users
#
#
# result = users(1, 'Toxir', 'Toxirov', 21, 'Fergana')
# print(result)

#-----------------------------------------------------------------------------------------------

# adminlar = [
#     {'id': 1, 'name': 'Toxir', 'lastname': 'Sobirov', 'password': '12345', 'address': 'Fergana', 'phone': 901234455},
#     {'id': 2, 'name': 'Bobur', 'lastname': 'Qodirov', 'password': '123', 'address': 'Andijon', 'phone': 934567788},
#     {'id': 3, 'name': 'Nodir', 'lastname': 'Toxirov', 'password': 'nodir123', 'address': 'Namangan', 'phone': 997865544}
# ]
#
#
# def admins(admins_list: list):
#     def inner(name):
#         return list(filter(lambda admin: admin['name'] == name, admins_list ))
#     return inner
#
# addmin = admins(adminlar)
#
# name1 = addmin('Toxir')
# print(name1)
#
# name2 = addmin('Nodir')
# print(name2)



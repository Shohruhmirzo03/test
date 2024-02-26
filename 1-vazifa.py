


# taomlar = ['manti', 'norin', 'chuchvara']
# taomlar.append('osh')
# taomlar.insert(1, 'mastava')
# taomlar_tuple = tuple(taomlar)
#
# print(taomlar_tuple)

#-----------------------------------------


# l = ["A", "a", "B", "b", "C", "c", "D", "d"]
# katta_h = [x for x in l if x.isupper()]
# kichik_h = [x for x in l if x.islower()]
# h_tuple = (katta_harflar, kichik_harflar)
# print(h_tuple)

#-----------------------------------------

# def davlat_nomerlari(numbers):
#     uz_numbers = []
#     ru_numbers = []
#     us_numbers = []
#
#     for number in numbers:
#         if number.startswith("+998"):
#             uz_numbers.append(number)
#         elif number.startswith("+7"):
#             ru_numbers.append(number)
#         elif number.startswith("+1"):
#             us_numbers.append(number)
#
#     return uz_numbers, ru_numbers, us_numbers
#
# p_numbers = ["+998991234567", "+79454874459", "+14385001031"]
# result = davlat_nomerlari(p_numbers)
# print(result)

# --------------------------------------------------------------------------

# def numbers(n):
#     royxat = [2 * i + 1 for i in range(n)]
#     return royxat
#
# n = 5  # Misol uchun, n soni
# royxat = numbers(n)
# print(royxat)

# -------------------------------------------------

# d = {'a': 1, 'b': 2, 'c': 3}
# yigindi = sum(d.values())
# print("Lug'at yigindisi:", yigindi)

# -------------------------------------------------
#
# d = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36}
# yigindi = sum(d.keys())
# print("Lug'at yigindisi:", yigindi)


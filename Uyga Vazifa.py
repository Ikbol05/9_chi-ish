# 1 va 2 chi masala
# tuple _ listga  uxshagan bitta funksiya. Tuple ni listdan farqi kamroq joy egallaydi masalan:
#
# python_group_tuple = ("Toxir", "Sobir", "Jalil", "Bakir", "Jamshid", "Nodir", "Sobir")
# python_group_list = ["Toxir", "Sobir", "Jalil", "Bakir", "Jamshid", "Nodir", "Sobir"]
#
# print(python_group_tuple.__sizeof__())
# print(python_group_list.__sizeof__())
#
# Tuple ni yana bir farqi undagi elementlarni uzgartrib  bulmaydi , uzgartirsa buladi ba'zi yullar bilan uzgartirsa buladi!

#-------------------------------------------------------------------------------------------------------------------------------------

# 3 chi masala

# n = int(input("Sonni kriting: "))
#
# summa = (range(1, n + 1, 1))
#
# print(tuple(summa))
#-------------------------------------------------------------------------------------------------------------------------------------
# 4 chi masala
#
# def kv (a):
#     return a ** 2
#
#
# n = int(input("Sonni kriting: "))
#
# summa = map(kv,range(1, n + 1, 1))
#
# print(tuple(summa))

#-------------------------------------------------------------------------------------------------------------------------------------

# 5 chi masala

# dict - lug'at  ya'ne malumot turi. dict ni {} yane yingalak qavsdan foydalaniladi

#-------------------------------------------------------------------------------------------------------------------------------------

# 6 chi masala

# dict ni listan farqi qavs ochi yopishda va dict da elementlarni ajratib yozishda : _ dan foydalaniladi



#-------------------------------------------------------------------------------------------------------------------------------------
# 7 chi masa

# user = {"first_name": "Abror", "last_name": "Ilyos", "adress": "Fergana"}
#
# while True:
#
#     for juft in user.keys():
#         pass
#
#     a = input("Kalitni kriting: ")
#
#     if juft == a:
#         print("Bunday kalit mavjud")
#     else:
#         print("Bunday kalit mavjud emas")

#-------------------------------------------------------------------------------------------------------------------------------------

# 8 chi masala

# d = {"a": 1, "b": 2, "c": 3}
#
# for qimmat in d.values():
#     pass
#
# javob = qimmat + qimmat
#
# print("Yug'indisi: ",javob)

#-------------------------------------------------------------------------------------------------------------------------------------

# 9 chi masala
#
# d = {1: 1, 2: 4, 3: 9, 4: 16, 5: 15, 6: 36}
#
#
# for yigindi in d.keys():
#     pass
#
# javob = yigindi + yigindi
#
# print("Javob: ", javob)
#-------------------------------------------------------------------------------------------------------------------------------------

# 10 chi masala

# J = {}
#
# n = int(input("Sonni kriting: "))
#
# for x in range(1, n + 1):
#     J[x] = (x, x * x)
#
# print(J)

#-------------------------------------------------------------------------------------------------------------------------------------

# 13 chi masala



# cities = {
#     'Moscow': (550, 370),
#     'London': (510, 510),
#     'Paris': (480, 480),
# }
#
# # Calculate distances
# moscow = cities['Moscow']
# london = cities['London']
# paris = cities['Paris']
#
# distances = {
#     'Moscow-London': ((moscow[0] - london[0])  2 + (moscow[1] - london[1])  2) ** 0.5,
#     'Moscow-Paris': ((moscow[0] - paris[0])  2 + (moscow[1] - paris[1])  2) ** 0.5,
#     'London-Paris': ((london[0] - paris[0])  2 + (london[1] - paris[1])  2) ** 0.5
# }
#
# print(distances)

#-------------------------------------------------------------------------------------------------------------------------------------


























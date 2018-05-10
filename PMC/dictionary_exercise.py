# 1----------------------------------------------------------------------------------------------------------------------
# This is a Python Program to add a key-value pair to a dictionary.

# dic = {}
#
# key = input("Enter the Key: ")
# value = input("Enter the Value: ")
#
# dic.update({key: value})
# print(f"Updated Dictionary is: {dic}")

# 2----------------------------------------------------------------------------------------------------------------------
# This is a Python Program to concatenate two dictionaries into a different dictionary.

# dic1 = {"a": 1, "b": 2}
# dic2 = {"c": 1, "d": 2}
# final_dic = {}
#
# for i, j in dic1.items():
#     final_dic.update({i: j})
#
# for i, j in dic2.items():
#     final_dic.update({i: j})
#
# print(f"Final Dictionary is: {final_dic}")

# 3----------------------------------------------------------------------------------------------------------------------
# This is a Python Program to check if a given key exists in a dictionary or not.
#
# info = {"name": "Touhid", "age": "21", "roll": 808516}
#
# key = input("Enter the Key: ")
#
# if key in info.keys():
#     print("{0} is {1}".format(key, info.get(key)))  # I can use info[key]
# else:
#     print("The key isn't here.")

# 4----------------------------------------------------------------------------------------------------------------------
# This is a Python Program to generate a dictionary that contains numbers (between 1 and n) in the form (x,x*x).
# dic = {}
# value = 0
# n = int(input("Enter The Element: "))
#
# for i in range(1, n + 1):
#     value = i
#     value = value * value
#     dic.update({i: value})
#
# print(dic)

# 5----------------------------------------------------------------------------------------------------------------------
#This is a Python Program to find the sum all the items in a dictionary.
# dic = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100}
# sum_of_dic = 0
# for i in dic.values():
#     sum_of_dic += i

# print(sum(dic.values())) # or i can use just it

# print("Total sum of Dictionary is {}".format(sum_of_dic))

# 6----------------------------------------------------------------------------------------------------------------------
# This is a Python Program to remove the given key from a dictionary
# dic = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100}
# print("Initial Dictionary is\n", dic)
# key = int(input("Enter the value to remove the key"))
#
# if key in dic.keys():
#     dic.pop(key)
#     # del dic[key] # i can use it
#     print("After removing\n", dic)
# else:
#     print("Key isn't found!!")

# 7----------------------------------------------------------------------------------------------------------------------
# This is a Python Program to form a dictionary from an object of a class.

# class Dictionary:
#     def __init__(self, first, last, age):
#         self.first = first
#         self.last = last
#         self.age = age
#
#
# dic_obj = Dictionary('Touhidur', 'Rahman', 21)
# print(dic_obj.__dict__)

# 8----------------------------------------------------------------------------------------------------------------------
# This is a Python Program to map two lists into a dictionary.
# lst1 = []
# lst2 = []
# dic = {}
#
# n1 = int(input("Enter the Element for Dictionary"))
# for i in range(1, n1 + 1):
#     key = int(input("Enter the element for Key: "))
#     lst1.append(key)
#
# n2 = int(input("Enter the Element for Dictionary"))
# for i in range(1, n1 + 1):
#     key = int(input("Enter the element for Value: "))
#     lst2.append(key)
#
# for key, value in zip(lst1, lst2):
#     dic.update({key: value})
#
# print(dic)

# 1----------------------------------------------------------------------------------------------------------------------
# This is a Python Program to add key-value pair to a dictionary.
# dic = {}
# n = int(input("Enter the element: "))
# {dic.update({input("Enter The Key"): input("Enter The Value")}) for i in range(1, n + 1)}
#
# print(dic)

# 2----------------------------------------------------------------------------------------------------------------------
# This is a Python Program to concatenate two dictionaries into a different dictionary.
# dic1 = {"a": 1, "b": 2}
# dic2 = {"c": 1, "d": 2}
# final_dic = {}
#
# {final_dic.update({i: j}) for i, j in dic1.items()}
# {final_dic.update({k: l}) for k, l in dic2.items()}
# print(final_dic)

# 3----------------------------------------------------------------------------------------------------------------------
# This is a Python Program to check if a given key exists in a dictionary or not.

# info = {"name": "Touhid", "age": "21", "roll": 808516}
# key = input("Enter the Key: ")
# x = {info[key] if key in info.keys() else print("The key isn't here!")}
# print(x)

# 4----------------------------------------------------------------------------------------------------------------------
# This is a Python Program to generate a dictionary that contains numbers (between 1 and n) in the form (x,x*x).
# dic = {}
# n = int(input("Enter The Element: "))
# x = {i: i * i for i in range(1, n + 1)}
# print(x)

# 5----------------------------------------------------------------------------------------------------------------------
# This is a Python Program to find the sum all the items in a dictionary.
# dic = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100}
# sum_of_dic = 0
#
# result = {sum(dic.values())}
# print("Total sum of Dictionary is {}".format(result))

# 6----------------------------------------------------------------------------------------------------------------------
# This is a Python Program to remove the given key from a dictionary
# dic = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100}
# print("Initial Dictionary is\n", dic)
# key = int(input("Enter The Key"))
# x = {dic.pop(key) if key in dic.keys() else print("Key isn't here!!")}
# print("After removing\n", dic)

# 8----------------------------------------------------------------------------------------------------------------------
# This is a Python Program to map two lists into a dictionary.
# lst1 = []
# lst2 = []
# dic = {}
# n1 = int(input("Enter the Element for Dictionary"))
# [lst1.append(input("Enter The Element For Key")) for i in range(1, n1 + 1)]
#
# n2 = int(input("Enter the Element for Dictionary"))
# [lst2.append(input("Enter The Element For Key")) for j in range(1, n2 + 1)]
#
# {dic.update({i: j}) for i, j in zip(lst1, lst2)}
#
# print(dic)

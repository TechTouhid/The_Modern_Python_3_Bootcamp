# join/concatenate two list in a different list

# a = [1, 2, 3, 4, 5, 6, 7]
#
# b = [10, 55, 65, 69, 33]
# empty_list = []
#
#
# # Method 1
# # Join two list using + operator
#
# # x = a + b
# # print(x)
#
#
# # Using list comprehension
# # Method 2
#
# [empty_list.append(i) for i in a] and [empty_list.append(j) for j in b]  # But i want t use only one list comprehension, is it possible?
#
# # Method 3
# # [(empty_list.append(i), empty_list.append(j)) for i, j in zip(a, b)] # only work when a and b has same length and it has a index problem
#
# print(empty_list)


# 1----------------------------------------------------------------------------------------------------------------------

# Python Program to Find the Largest Number in a List

n = int(input("Enter the number of element"))
lst = []

for i in range(1, n + 1):
    value = int(input("Enter the element: "))
    lst.append(value)

print('The largest number is', max(lst))


# 2----------------------------------------------------------------------------------------------------------------------
# Python Program to Find the Second Largest Number in a List

# n = int(input("Enter the number of element"))
# lst = []
#
# for i in range(1, n + 1):
#     value = int(input("Enter the element: "))
#     lst.append(value)
#
# lst.sort()
# print('The largest number is', lst[n - 2])

# 3----------------------------------------------------------------------------------------------------------------------

# Input coma, space separated value in list

# lst = []
# value = input("Enter the element: ").split(sep=' ')
# lst.extend(value)
#
# print(max(list(map(int, lst))))

# 4----------------------------------------------------------------------------------------------------------------------
# This is a Python Program to put the even and odd elements in a list into two different lists.

# n = int(input("Enter the number of element"))
# even = []
# odd = []
# number = []
#
# for i in range(1, n + 1):
#     value = int(input("Enter the element: "))
#
#     number.append(value)
#
# print(number)
# for i in number:
#     if i % 2 == 0:
#         even.append(i)
#     else:
#         odd.append(i)
#
# print(f"even numbers are {even}")
# print(f"Odd numbers are {odd}")

# 5----------------------------------------------------------------------------------------------------------------------

# Python Program to Merge Two Lists and Sort it

# lst1 = []
# lst2 = []
#
# n1 = int(input("Enter the number of element in list 1"))
#
# for i in range(1, n1 + 1):
#     value = int(input("Enter the elements"))
#     lst1.append(value)
# print("-----------------------------------------------")
# n2 = int(input("Enter the number of element in list 2"))
# for i in range(1, n2 + 1):
#     value = int(input("Enter the elements"))
#     lst2.append(value)
#
# x = lst1 + lst2
# x.sort()
# print(x)

# 6----------------------------------------------------------------------------------------------------------------------
# The program takes a list and sorts the list according to the length of the elements.
# lst1 = []
# n1 = int(input("Enter the number of element in list 1"))
#
# for i in range(1, n1 + 1):
#     value = input("Enter the elements")
#     lst1.append(value)
#
# lst1.sort(key=len)      # sort list using the length word
# print(lst1)


# 7----------------------------------------------------------------------------------------------------------------------
# Python Program to Find the Union of a list
# a = []
# n = int(input("Enter the number of elements in list:"))
# for x in range(0, n):
#     element = int(input("Enter element" + str(x + 1) + ":"))
#     a.append(element)
# union = set(a)
# print("The original list is: ", a)
# print("The new list is: ", list(union))

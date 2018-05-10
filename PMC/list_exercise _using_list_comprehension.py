# 1----------------------------------------------------------------------------------------------------------------------
# Python Program to Find the Largest Number in a List

# lst = []
# n = int(input("Enter the number of element"))
# [lst.append(input("Enter the element: ")) for i in range(1, n + 1)]
# print(max(lst))


# 2----------------------------------------------------------------------------------------------------------------------

# Python Program to Find the Second Largest Number in a List

# lst = []
# n = int(input("Enter the number of element"))
# [lst.append(input("Enter the element: ")) for i in range(1, n + 1)]
# lst.sort()
#
# print(lst[n - 2])

# 3----------------------------------------------------------------------------------------------------------------------

# This is a Python Program to put the even and odd elements in a list into two different lists.
# even = []
# odd = []
# number = []
#
# n = int(input("Enter the number of element"))
# [number.append(int(input("Enter the element: "))) for i in range(1, n + 1)]
# [even.append(i) for i in number if i % 2 == 0]
# [odd.append(i) for i in number if i % 2 != 0]
#
# print(even)
# print(odd)

# 4----------------------------------------------------------------------------------------------------------------------

# Python Program to Merge Two Lists and Sort it
# empty_list = []
# lst1 = []
# n = int(input("Enter the number of element for list 1 "))
# [lst1.append(input("Enter the element: ")) for i in range(1, n + 1)]
#
#
# lst2 = []
# n = int(input("Enter the number of element for list 2"))
# [lst2.append(input("Enter the element: ")) for j in range(1, n + 1)]
#
# [empty_list.append(i) for i in lst1] and [empty_list.append(j) for j in lst2]
#
# empty_list.sort()
# print(empty_list)

# 5----------------------------------------------------------------------------------------------------------------------
# The program takes a list and sorts the list according to the length of the elements.
# lst1 = []
# n = int(input("Enter the number of element "))
# [lst1.append(input("Enter the element: ")) for i in range(1, n + 1)]
# lst1.sort(key=len)
# print(lst1)

# 6----------------------------------------------------------------------------------------------------------------------
# Python Program to Find the Union of a list
lst1 = []
n = int(input("Enter the number of element "))
[lst1.append(int(input("Enter the element: "))) for i in range(1, n + 1)]
union = list(set(lst1))
print(union)

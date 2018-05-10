# patern = "\U0001f600"
#
# for i in range(1, 11):
#     print(patern * i)
#
# print(dir(dict))


num = int(input("Enter the number of rows:"))
for i in range(0, num):
    for j in range(0, num - i - 1):
        print(end=" ")
    for j in range(0, i + 1):
        print("*", end=" ")
    print()




































# Right angle triangle shape


# num = int(input("Enter the number to rows!"))
#
# k = 0
#
# for i in range(1, num + 1):
#     for j in range(1, k + 1):
#         print("*", end=" ")
#     k +=2
#     print()


# print Pyramid

#num = int(input("Enter the of rows!"))

num = [5, 7, 9, 8, 10]
for n in num:
    for i in range(0, n):
        for j in range(0, n - i - 1):
            print(end=" ")
        for k in range(0, i + 1):
            print("*", end=" ")
        print()
    print()
















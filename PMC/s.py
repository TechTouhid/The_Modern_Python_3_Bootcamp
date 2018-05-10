#
# n=6
# i = 0
# while (i < n):
#     sum_lst = input().split()
#     lst = []
#     x = sum_lst
#     lst.append(x)
#     print(lst[i])
#     i=i+1
#
#
#
# print(lst)
# print(sum(lst))






# lst = input().split()
# print(lst)
# lsts = []
# for i in lst:
#     lsts.append(int(i))
#
# print(sum(lsts))


# i = 0
#
# while i < 6:
#     lst = input().split()
#     lsts = []
#     lsts.append(int(i))
#     print(sum(lsts))
#     i = i + 1


# for i in range(6):
#     lst = input()
#     lsts = []
#     lsts.append(i)
# print(lsts)


# Using range with user input
# time = input("How many times do I have to tell you? \n")
# time = int(time)
#
# for i in range(time):
#     print("Cleane up your room")


# remove extra line form code and make it more efficient
for num in range(1,21):
    if num == 4 or num == 13:
        status = "Unlucky"
    elif num % 2 == 0:
        status = "Even"
    else:
        status = "Odd"

    print(f"{num} is {status}")


















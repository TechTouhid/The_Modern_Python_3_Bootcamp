n = int(input())

for i in range(1, n + 1):
    S = input()

    print("{0} {1}".format(S[0:len(S):2], S[1:len(S):2]))

# for j in S:
#     if S.index(j) % 2 == 0:
#         print(j, end=' ')
#     # else:
#     #     print(j)

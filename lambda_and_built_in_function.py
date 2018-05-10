a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
b = [2, 4, 8, 10]
#  use of lambda and map function

# test = map(lambda x: x * 2, a)
#
# print(list(test))

# use of filter function

# test_filter = filter(lambda x: x % 2 == 0, a)
# print(list(test_filter))

# b = 5
#
# print(not b == 5)

# # use of all
# test_all = all([i for i in b if i % 2 == 0])
#
# print(test_all)

# use of any
test_any = any([i for i in a if i % 2 == 0])

print(test_any)


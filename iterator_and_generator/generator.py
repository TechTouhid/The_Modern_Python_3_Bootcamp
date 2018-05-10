def count_up_to_max(max):
    count = 1
    while count <= max:
        yield count
        count += 1


value = count_up_to_max(5)
# print(next(value))
for i in value:
    print(i)

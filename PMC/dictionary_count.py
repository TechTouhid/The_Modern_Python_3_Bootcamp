#
# dic = {"name": "Touhid", "add":"natore"}
#
# for i, j in dic.items():
#     print(i, j)


d = [{"abc":"movies"}, {"abc": "sports"}, {"abc": "music"}, {"xyz": "music"},
     {"pqr":"music"}, {"pqr":"movies"},{"pqr":"sports"}, {"pqr":"news"},
     {"pqr":"sports"}, {"touhid":"alamin"}, {"raisul":"alamin"}]

# from collections import Counter
# counts = Counter(value for dic in d for value in dic.values())
# print(dict(counts))


# Counter({'pqr': 5, 'abc': 3, 'xyz': 1})
# for value in counts:
#     print (value, counts[key])

# search = input("Enter your Word.\n")
# count = 0
#
# for dic in d:
#     for value in dic.values():
#         if value == search:
#             count = count + 1
#
#
# print(search + " " + str(count))


# d = {}
#
# lst = ['alamin', 'raisul', 'alamin', 'raisul']
# search = input("Enter your Word: ")
# count = 0
# for value in lst:
#     if value == search:
#         count = count + 1
#
# d[search] = count
#
# print(d)

n = int(input())
phoneBook = {}

for i in range(1, n + 1):
    arr = [arr_temp for arr_temp in input().strip().split(' ')]
    keys = str(arr[0])
    values = int(arr[1])
    phoneBook.update({keys: values})


for i in range(1, n + 1):
    key = input()
    if key in phoneBook.keys():
        print("{0}={1}".format(key, phoneBook[key]))
    else:
        print("Not found")

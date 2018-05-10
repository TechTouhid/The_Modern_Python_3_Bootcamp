import time


# def my_for(iterable, func):
#     iterator = iter(iterable)
#     while True:
#         try:
#             thing = next(iterator)
#         except StopIteration:
#             # print("End of iterator!")
#             break
#         else:
#             func(thing)
#
#
# def square(x):
#     print(x * x)


# my_for([1, 2, 3, 4, 5, 6], square)


# class Counter:
#     def __init__(self, low, high):
#         self.current = low
#         self.high = high
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.current < self.high:
#             # num = self.current
#             self.current += 1
#             return self.current
#         raise StopIteration
#
#
# # c = Counter(0, 10)
# # iter(c)
#
# for x in Counter(50, 60):
#     print(x)


# infinite generator

# def current_beat():
#     nums = (1, 2, 3, 4)
#     i = 0
#     while True:
#         if i >= len(nums): i = 0
#         yield nums[i]
#         i += 1
#
# for x in current_beat():
#     print(x)

# Testing memory using generator

# def fib_list(max):
#     nums = []
#     a, b = 0, 1
#     while len(nums) < max:
#         nums.append(b)
#         a, b = b, a + b
#     return nums
#
#
# print(fib_list(10))


# def fib_gen(max):
#     x = 0
#     y = 1
#     count = 0
#     while count < max:
#         x, y = y, x + y
#         yield x
#         count += 1
# for i in fib_gen(1000000):
#     print(i)

# Generator expressions and speed test

gen_start_time = time.time()
print((sum(n for n in range(1000000))))
gen_time = time.time() - gen_start_time

list_start_time = time.time()
print((sum([n for n in range(1000000)])))
list_time = time.time() - gen_start_time


print(f'(sum(n for n in range(1000))) took: {gen_time}')
print(f'(sum(n for n in range(1000))) took: {list_time}')

# List comprehension
# Syntax [statement for variable_for_loop in iterator] / [_____ for _____ in ____]


nums = [1, 2, 3, 4, 5]
#
# value = [i * 10 for i in nums]
# print(value)

# Using conditional logic

even = [i for i in nums if i % 2 == 0]
odds = [i for i in nums if i % 2 != 0]

print(even, odds)


other = [i * 2 if i % 2 == 0 else i / 2 for i in nums]

# using .join

with_voels = "This is so much fun!"

print(''.join(char for char in with_voels if char not in 'aeiou'))
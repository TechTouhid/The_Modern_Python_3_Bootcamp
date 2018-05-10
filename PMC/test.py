# def cal_func(x):
#     if x == 1:
#         return 1
#     else:
#         return (x * cal_func(x -1))
#
# print(cal_func(4))

#
# class A:
#     def name(self):
#         print("Define in class A")
#
#
# class B:
#     # def name(self):
#     #     print("Define in Class B")
#     pass
#
# class C(B, A):
#     # def name(self):
#     #     print("Define in class C")
#     pass
#
#
# obj = C()
#
# obj.name()

# class Pizza:
#     def __init__(self, toppings):
#         self.toppings = toppings
#
#     @staticmethod
#     def validate_topping(topping):
#         if topping == "pineapple":
#             raise ValueError("No pineapples!")
#         else:
#             return True
#
#
# ingredients = ["cheese", "onions", "spam", "apple"]
# if all(Pizza.validate_topping(i) for i in ingredients):
#     pizza = Pizza(ingredients)

# property

from collections import namedtuple

# d = {"name": "Touhid", "roll": 10, "reg": 77777}
# d.update({"first":"T"})

point = namedtuple('point', ['name', 'roll', 'reg'])
value = point("Touhid", 10, 7654)
value2 = point("Raisul", 10, 7654)



# print(value.name, value.roll)

print(value)
print(value2)
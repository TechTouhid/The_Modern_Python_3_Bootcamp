# String formatting options
# guess = 8
#
# print(f'your guess of {guess} was incorrect!')
# print('your guess of {0} was incorrect!'.format(guess))
# print("your guess of %d was incorrect!" % guess)

# A simple program to convert kilometer to miles
# input_kilometer = input("How many kilometer did you cycle today?\n")
#
# miles = int(input_kilometer) / 1.60934
# miles = round(miles, 2)
# print("You cycle {} miles today.".format(miles))

# age = 77
#
# if not ((age >= 2 and age <= 8) or age >= 65):
#     print("You pay $10 you are not a child.")
# else:
#     print("You pay $5 you are an adult")











#-----------------------------Methode Overwriting
# class Father:
#     def print_firstname(self):
#         print("Father name")
#
#     def print_lastname(self):
#         print("Last name")
#
# class Son(Father):
#     def print_firstname(self):
#         print("Touhid")
#
#     pass

# obj_father = Father()
#
# obj_father.print_firstname()

# obj_son = Son()
#
# obj_son.print_firstname()
# obj_son.print_lastname()








#-----------------------------Methode Overloding
# class Father:
#     def add(self, *args):
#         result = 0
#
#         for i in args:
#             result = result +i
#         return result
#
# obj = Father()
# print(obj.add(1,2,3))
#
# print(obj.add(1,2,3,4,5,6,7,8,9))


# --------------------------python dimond problem
class Base1():
    def m(self):
        print("Class Base1")


class Base2():
    def m(self):
        print("Class Base2")


class Left(Base1):
    # def m(self):
    #     print("Class Left")
    pass


class Right(Base1):
    # def m(self):
    #     print("Class Right")
    pass


class Join(Right, Left):
    # def m(self):
    #     print("Class Join")
    pass


obj = Join()
obj.m()

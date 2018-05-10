# def be_polite(fn):
#     def wrapper():
#         print("What a pleasure to meet you!")
#         fn()
#         print("Have a greet day!")
#     return wrapper
#
# @be_polite
# def greet():
#     print("My name is Touhid")
#
# @be_polite
# def rage():
#     print("I hate you!")
#
# greet()
# print('------------------')
# rage()
#
# # ploite_rage = be_polite(rage)
# # greet()
# # print()
# # ploite_rage()

# Decorator with different signature

def shout(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs).upper()
    return wrapper

@shout
def greet(name):
    return f'Hi I\'m {name}'


@shout
def order(main, side):
    return f"Hi, I'd like the {main}, with a side of {side}, please."


print(greet('Touhid'))
print(order('burger', 'fries'))
# Working with single value *
# Define Function here


# def sum_of_number(*number):
#     result = 0
#     for i in number:
#         result += i
#     return result
#
#
# # Printing and calling the function
# print(sum_of_number(1, 2, 3, 4, 5))

# Working with Dictionary **


def favrite_color(**fcolor):

    #for person, color in fcolor.items():
    for person, color in zip(fcolor, fcolor):

        print(f"{person}'s color is {color}")

favrite_color(Touhid="Red", Bithy="Blue", Samira="green", Raisul="pink")

   
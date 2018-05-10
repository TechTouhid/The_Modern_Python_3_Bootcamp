import time

import pyfiglet
from termcolor import colored

message = input("Enter a Text ")
color = input("Enter a color ")
colored_art = pyfiglet.figlet_format(message)
colored_art = colored(colored_art, color=color)
print(colored_art)



# import sys
# import time
#
# def blink_once():
#     sys.stdout.write('\rTEXT')
#     time.sleep(0.5)
#     b = ("Loading")
#     sys.stdout.write('\r     ')
#     time.sleep(0.5)
#
# def blink(number):
#     for x in range(0,number):
#         blink_once()
#
# blink(5)















# x = int(input("Enter a number"))
# for i in range(1, 11):
#
#     result = i * x
#     print(f'{x} x {i} = {result}')




# age = int(input("Enter your birth year: "))
#
# your_age = 2018 - age
# print(f'you are {your_age} years old...')





# neme = input("enter your neme")
#
# print("hello " + neme)








# name=input("enter your name")
#
# print("pagol " +name )














# print(f'you are {your_ag
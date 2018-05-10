import logging

logging.basicConfig(filename="simple2.log", level=logging.INFO, format="%(levelname)s: %(asctime)s :%(message)s")


def add(x, y):
    return logging.info(f"Sum of {x} + {y} = {x+ y}")


def mul(x, y):
    return logging.info(f"Mul of {x} * {y} = {x * y}")


def div(x, y):
    return logging.info(f"Div of {x} / {y} = {x / y}")


num1 = 20
num2 = 5

(add(num1, num2))
(mul(num1, num2))
(div(num1, num2))

from random import choice


# Higher Order functions

def greet(person):
    def mode():
        msg = choice(('Hello there ', 'Go away ', 'I love you '))
        return msg

    result = mode() + person
    return result

print(greet("Touhid"))

class Info:

    def __init__(self, first, last, age):  # Method to be execute first
        self.first = first  # Variable declaration inside a class
        self.last = last
        if age >= 0:
            self._age = age
        else:
            self._age = 0

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if value >= 0:
            self._age = value
        else:
            raise ValueError("Age can't be negative!")


jane = Info("Jane", "Goodall", 12)

print(jane.age)
jane.age = - 20
print(jane.age)

#  Example 2

class Pizza:
    def __init__(self, topping):
        self.topping = topping
        self._pineapple_allowed = False

    @property
    def pineapple_allowed(self):
        return self._pineapple_allowed

    @pineapple_allowed.setter
    def pineapple_allowed(self, value):
        if value:
            password = input()
            if password == "touhid":
                self._pineapple_allowed = value
            else:
                raise ValueError("Alert! Intruder!")



pizza = Pizza(["cheese", "tomato"])
print(pizza.pineapple_allowed)
pizza.pineapple_allowed = True
print(pizza.pineapple_allowed)

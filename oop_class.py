# Creating a class

class Info():

    active_user = 0  # Class attribute

    @classmethod                                                            # Class method
    def display_active_user(cls):
        return f"There are {cls.active_user} active users!"

    def __init__(self, first, last, age):  # Method to be execute first
        self.first = first  # Variable declaration inside a class
        self.last = last
        self.age = age
        Info.active_user += 1

    def fullname(self):
        return f"{self.first} {self.last}"

    def initials(self):
        return f"{self.first[0]}.{self.last[0]}"

    def things(self, thing):
        return f"{self.first} likes {thing}"

        # self._msg = 'hhhhhhh'      # Protected member but accessible
        # self.__msg = 'eeeeeeeeeee'  # Protected member not accessible
        #


i = Info('Touhid', 'Rahman', 21)  # Create a object for Info class
i2 = Info('Touhid', 'Rahman', 21)
#
# print(i.fullname())
# print(i.initials())
# print(i.things('Technology'))

# print(i.first, i.last, i.age)         # Calling variable from class using i object
# print(i2.first, i2.last, i2.age, i._msg)


print(Info.display_active_user())

i = Info('Touhid', 'Rahman', 21)  # Create a object for Info class
i2 = Info('Touhid', 'Rahman', 21)
print(Info.display_active_user())
i3 = Info("partho", "vai", 89)
print(i3.first)
i3.first = "Partho"
print(i3.fullname())


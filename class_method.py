# Creating a class

class Info():


    active_user = 0
    @classmethod
    def display_active_user(cls):
        return f"There are {cls.active_user} active users!"

    @classmethod
    def from_string(cls, data_str):
        first, last, age = data_str.split(',')
        return cls(first, last, age)

    def __init__(self, first, last, age):  # Method to be execute first
        self.first = first      # Variable declaration inside a class
        self.last = last
        self.age = age
        Info.active_user += 1

    def fullname(self):
        return f"{self.first} {self.last}"

    def initials(self):
        return f"{self.first[0]}.{self.last[0]}"

    def things(self, thing):
        return f"{self.first} likes {thing}"


name = Info.from_string("Touhid,alamin,21")


print(name.first)
print(name.fullname())
print(name.initials())




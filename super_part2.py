# Creating a class

class User():
    active_user = 0  # Class attribute

    @classmethod                                                            # Class method
    def display_active_user(cls):
        return f"There are {cls.active_user} active users!"

    def __init__(self, first, last, age):  # Method to be execute first
        self.first = first  # Variable declaration inside a class
        self.last = last
        self.age = age
        User.active_user += 1

    def fullname(self):
        return f"{self.first} {self.last}"

    def initials(self):
        return f"{self.first[0]}.{self.last[0]}"

    def things(self, thing):
        return f"{self.first} likes {thing}"

class Moderator(User):
    def __init__(self, first, last, age, community):
        super().__init__(first, last, age)
        self.community = community

    def remove_post(self):
        return f"{self.fullname()} remove a post form the {self.community} community."


user = Moderator("Touhid", "alamin", 21, "Divine IT Limited")

print(user.remove_post())

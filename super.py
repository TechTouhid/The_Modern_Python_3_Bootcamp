# Use of super in inheritance

class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species


class Cat(Animal):
    def __init__(self, name, species, bred, toy):
        super().__init__(name, species)             # Use of super class
        # Animal.__init__(self, name, species)      # Similar like super class
        self.bred = bred
        self.toy = toy
        # self.name = name                          # When use super class no need to use those duplicate lines
        # self.species = species

    def __repr__(self):
        return f"Animal info is {self.name} is {self.species} bred is {self.bred} toy is {self.toy}"


info = Cat("Akkas", "Cat", 'Ruti', 'String')

print(info)
print(info.species)
print(info.name)


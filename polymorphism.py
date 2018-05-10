class Human:
    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        self.age = age

    def __repr__(self):
        return f"Human named {self.first} {self.last}"

    def __add__(self, other):
        print(isinstance(other, Human))
        if isinstance(other, Human):
            return Human(first='Sad', last='Eamin', age=10)
        return 'You can\'t do this'


H = Human('Touhid', 'alamin', 21)
I = Human('Touhid', 'alamin', 21)

print(H)
print(H + 2)

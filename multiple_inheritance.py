class A:
    def do_something(self):
        print("Define in A")


class B(A):
    def do_something(self):
        print("Define in B")


class C(A):
    def do_something(self):
        print("Define in C")


class D(B, C):
    def do_something(self):
        print("Define in D")

class X(A):
    print("sfklskfjsk")



inharit = D()
# inharit.dosomething()

# print(D.mro())
# print(D.__mro__)
print(help(D))

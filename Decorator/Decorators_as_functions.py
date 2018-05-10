def be_polite(fn):
    def wrapper():
        print("What a pleasure to meet you!")
        fn()
        print("Have a greet day!")
    return wrapper


def greet():
    print("My name is Touhid")


def rage():
    print("I hate you!")

greet = be_polite(greet)
ploite_rage = be_polite(rage)
greet()
print()
ploite_rage()
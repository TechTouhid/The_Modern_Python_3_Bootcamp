def be_polite(fn):
    def wrapper():
        print("What a pleasure to meet you!")
        fn()
        print("Have a greet day!")
    return wrapper

@be_polite
def greet():
    print("My name is Touhid")

@be_polite
def rage():
    print("I hate you!")

greet()
print('-------------------')
rage()
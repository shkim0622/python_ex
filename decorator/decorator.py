def my_decorator(func):
    def wrapper():
        print("befor")
        func()
        print("After")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()

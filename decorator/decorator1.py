# my_decorator 함수는 다른 함수를 매개변수로 받음
# 함수를 수정하여 새로운 동작을 추가하는 역할
def my_hello():
    print("hello world@")

def wrapper(func):
    print("hello world")
    func()
    print("hello2 world")


def my_decorator(func):
    #wrapper(func)   
    # def wrapper():
    #     print("hello world")
    #     func()
    #     print("hello2 world")

    return wrapper


# func1 함수가 실행될 때 my_decorator 함수가 적용
@my_decorator
def myfunc():
    print("HELLO!!!")
    
myfunc()
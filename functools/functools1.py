import functools

def my_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print("Decorator 시작")
        return func(*args, **kwargs)
    return wrapper

@my_decorator
def my_function():
    """함수 실행 예제"""
    print("Function 시작")

my_function()
print("Function name:", my_function.__name__)
print("Function doc:", my_function.__doc__)

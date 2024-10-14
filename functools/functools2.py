import functools

def func(x, y):
    return x * y

A = functools.partial(func, y=2)  # y를 2로 고정한 새로운 함수 생성
B = functools.partial(func, y=3)  # y를 3로 고정한 새로운 함수 생성

print("A of 3:", A(3))
print("B of 3:", B(3))
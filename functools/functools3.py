import functools

num = [1, 2, 3, 4, 5]
sum = functools.reduce(lambda x, y: x + y, num)
print("Sum number:", sum)
import time

def func(n):
    if n == 0:
        return 0 
    elif n == 1 or n ==2 :
        return 1
    else:
        return func(n-1)+func(n-2)

s0 =time.time()
print(func(40))
s1 =time.time()


print("time : ", s1-s0)
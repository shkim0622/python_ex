import time 

def my_func(n):
    if n==0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return my_func(n)+my_func(n-1)
    
start = time.time()
print(my_func(10))
end = time.time()
print("time : ",end -start)
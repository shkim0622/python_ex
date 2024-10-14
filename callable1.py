#함수 callable 호출
def func():
    print('hello world')
func()
print(callable(func)) # true


#객체 callable 호출
class func2():
    def __init__(self,name):
        self.name=name
my_func2=func2('red')
print(callable(my_func2))  #false

#객체 __call__ callable 호출
class func3:
    def __init__(self,name):
        self.name=name
    def __call__(self):
        print('name {}'.format(self.name))

my_func3=func3('blue')
my_func3()

print(callable(func3))  #true
print(callable(my_func3))   #true


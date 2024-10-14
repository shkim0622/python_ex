class func:
    def __init__(self, name):
        self.name= name
        
    def __enter__(self ):
        print('start')
        
    def __exit__(self, type, value,trackback):
        print('end')
        
    def myfunc(self):
        print('my name is {}'.format(self.name))
        
f1=func('red')
with f1:
    f1.myfunc()
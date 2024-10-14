class Num:
    def __init__(self,data):
        self.data=data
    
    def __getitem__(self,key):
        print('__getitem__', key)
        return self.data[key]
   
    def __setitem__(self,key,val):
        print('__getitem__: ',key,val)
        self.data[key]=val
    
    def __delitem__(self,key):
        print('__delitem__',key)
        del self.data[key]
            
a = Num([1,2,3,4,5])
print(a[2])
print(a.data)
print('-----------------')

a[0] = 'a'
a[1] = 'b'
a[2] = 'c'
a[3] = 'd'
a[4] = 'e'
print(a.data)
print('-----------------')

del a[2]
print(a.data)


class Num:
    def __init__(self,data):
        self.data=data

    def __delitem__(self,key):
        del self.data[key]
        
a = Num([1,2,3,4,5])
del a[2]
print('del a[2] : ',a.data)

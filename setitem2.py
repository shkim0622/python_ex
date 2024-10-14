class Num:
    def __init__(self,data):
        self.data=data

    def __setitem__(self,key,val):
        self.data[key]=val
        
a = Num([1,2,3,4,5])
print('org data : ',a.data)

a[0] = 'a'
a[1] = 'b'
a[2] = 'c'
a[3] = 'd'
a[4] = 'e'
print('new data : ',a.data)

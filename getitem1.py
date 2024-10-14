class Num(list):
    def __init__(self, data):
        self.data = data
       
    def __getitem__(self,key):
        return self.data[key]

a = Num([1,2,3,4,5,6,7])
print('a[2:5] : ',a[2:5])
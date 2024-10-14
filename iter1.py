class Iter1:
    def __init__(self,data):
        self.data= data
        self.num = 0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.num < self.data:
            val = self.num
            self.num+=1
            return val
        else:
            raise StopIteration
        
for i in Iter1(5) :
    print(i)
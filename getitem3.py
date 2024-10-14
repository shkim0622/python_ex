class Num:
    def __init__(self):
        self.data = [n for n in range(1,10)]
       
    # def __getitem__(self,idex):
    #     return self.data[idex]

a = Num()
print(a.data[2:5])


from collections import ChainMap

class Map:
    def __init__(self, *maps):
        self.chain = ChainMap(*maps)
    
    def __repr__(self):
        return f'chian = {self.chain}'
            
d1 = {'a':1,'b':2}
d2 = {'c':3,'d':4}
d3 = {'e':7,'f':6}

chain1= Map(d1,d2)

print('chainmap(d1,d2) : ')
print(chain1.maps)

chain2 = chain1.new_child(d3)
print('new chainmap(d1,d2,d3) : ')
print(chain2.maps)

print(chain2['b'])
chain2.maps = reversed(chain2.maps) 
print(chain2.maps)
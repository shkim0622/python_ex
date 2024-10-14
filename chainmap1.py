from collections import ChainMap

d1 = {'a':1,'b':2,'a':3}
d2 = {'c':3,'d':4}
d3 = {'e':7,'f':6,'a':1}

chain1= ChainMap(d1,d2)

print('chainmap(d1,d2) : ')
print(chain1.maps)

chain2 = chain1.new_child(d3)
print('new chainmap(d1,d2,d3) : ')
print(chain2.maps)

print('chain2[b] : ',chain2['b'])

for key,value in chain2.items():
    print(key,"--->",value)

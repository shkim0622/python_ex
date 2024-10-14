from collections import namedtuple

Person = namedtuple('Person', ['name', 'age'])

def func(name,age):
    if age ==1:
        return Person('A',1)
    elif age ==2:
        return Person('B',2)
    else:
        return Person('None',0)

person1=func('A',1)

print(person1)
print(person1.name)
print(person1.age)

from collections import namedtuple

Person = namedtuple('Person', ['name', 'age'])

person1 = Person(name='A', age=1)
person2 = Person(name='B', age=2)

print(person1)
print(person1.name)  
print(person1.age) 

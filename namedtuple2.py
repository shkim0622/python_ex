class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __str__(self):
        return f'name={self.name},age={self.age}'
        
person1 = Person(name='A', age=1)
person2 = Person(name='B', age=2)

print(person1)
print(person1.name) 
print(person1.age) 


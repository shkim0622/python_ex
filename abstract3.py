from abc  import *
class humanbase(metaclass=ABCMeta):
    @abstractmethod
    def eat(self):
        pass
    
    @abstractmethod
    def work(self):
        pass

class human(humanbase):
    def __init__(self,name,*arg):
        self.name=name
        print('my name is {}'.format(name))
        
    def eat(self,food):
        print('{} eats {}'.format(self.name,food))
        
    def work(self,job):
        print('{} do {} work'.format(self.name,job))
        

a=human('banana')
a.eat('apple')
a.work('programming')
    

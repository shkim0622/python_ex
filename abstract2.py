from abc import*

class Abstractclass(metaclass=ABCMeta):
    name="이름"
    age="나이"
    
    def show():
        print("Abstract method")
    
    @abstractmethod
    def show_age(self):
        print("age??")
    
    
        
class myclass(Abstractclass):
    def __init__(self,name,age):
        self.name=name
        self.age=age
        
    def show_name(self):
        print("이름 : ",self.name)
        
    def show_age(self):
        super().show_age()
        print("나이 :" ,self.age )

if __name__=='__main__'
a= Abstractclass
a.show()

c=myclass('abc',100)
c.show_name()
c.show_age()
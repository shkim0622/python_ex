from abc import*

class Abstractclass(metaclass=ABCMeta):
    name="이름"
    age="나이"
    
    def show():
        print("국가 클래스 메소드이다.")
        
class myclass(Abstractclass):
    def __init__(self,name,age):
        self.name=name
        self.age=age
        
    def show_name(self):
        print("이름 : ",self.name)
        
a= Abstractclass
a.show()

c=myclass('abc',100)
c.show_name()

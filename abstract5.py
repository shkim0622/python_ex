from abc import *

class human(ABCMeta): 
    #추상메소드
    @abstractmethod
    def walk(self):
        print('human walk !!')
     
    #추상메소드   
    @abstractmethod
    def talk(self):
        pass
    
    #일반메소드
    def sleep(self):
        print('human sleep ! !')
        
class child(human):
    def walk(self):
        print('child walk !!')
      
class baby(human):
    def walk(self):
        print('baby walk !! ')
    
    def talk(self):
        print('baby talk !! ')         
        
#h1=human()     error      
#Human 클래스를 객체로 만들려고 했지만 에러
#c1=child()     error      
#추상 메서드를 모두 재정의 하지 않은 Adult 클래스 또한 객체로 만들려 시도할때에러가 발생

b1 = baby()     
#모든 추상 메서드를 구현한 Baby 클래스만 객체를 생성
b1.walk()
b1.talk()
b1.sleep()

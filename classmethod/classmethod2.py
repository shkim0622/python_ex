class MyClass:
    myc = "Hello, Class!"

    def __init__(self, value):
        self.value = value

    @classmethod
    # 클래스 메서드로서 클래스 자체를 첫 번째 인자로 받아와서 클래스 변수인 myclass에 접근
    def class_method(cls,val):
        cls.myc = cls.myc + val

        return cls.myc

    @staticmethod
    # 정적 메서드로서 클래스나 인스턴스와는 무관하게 독립적으로 동작
    def static_method():
        return "This is a static method"
    
    def my_method(self):
        pass
        # print(myc)

# 인스턴스 생성 및 속성 출력
obj = MyClass("Hello")
obj2 =MyClass("Hello2")
print(obj.value)
obj.my_method()
print(MyClass.class_method("10"))
print(obj.class_method("20"))
print(obj.static_method()) 
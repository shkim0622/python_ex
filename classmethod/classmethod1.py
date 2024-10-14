class Car:
    count = 0
    
    def __init__(self, name):
        self.name = name
        Car.count += 1

    # 클래스 메서드 생성
    @classmethod
    def outcount(cls):
        print('지금까지 총 {}대의 자동차 인스턴스가 생성되었습니다'.format(cls.count))
        
# 자동차 인스턴스 1개 생성
genesis = Car('제네시스')
print(Car.outcount())

# 자동차 인스턴스 추가 생성
ionic = Car('아이오닉')
print(Car.outcount()) 

eclass = Car('E클래스')
print(Car.outcount()) 
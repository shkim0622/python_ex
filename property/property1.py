class Citizen:
    def __init__(self, age_value):
        self._age = age_value

    @property
    def age(self,age_val):
        print("나이를 리턴합니다.")
        self._age =  age_val
        return self._age
    
    # @age.getter
    # def age2(self):
    #     print("age_getter")
    #     return self._age
    
    @age.setter
    def age(self, age_value):
        print("나이를 새로 설정합니다.")
        self._age = age_value


citizen = Citizen(20)
# print(citizen.age2)

citizen.age = 30
# print(citizen.age)
#age 변수의 값을 읽는 것이 아니라 바로 아래의 age 메소드가 실행
#age 메소드 위에 붙은 @property 데코레이터 때문

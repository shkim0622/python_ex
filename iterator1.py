list1=[1,2,3,4]

for i in list1:     #내부적으로 __iter__() 호출 후 1번만 순회하고 stop
    print('one :',i)
    
for i in list1:     ##내부적으로 __iter__() 호출 후 1번만 순회하고  stop
    print('two : ' ,i)
print('-----------------')

iter1 = list1.__iter__()    #list1.__iter__() 반복자 생성하여 1번만 for문 순회
                            #2번째 for문에서는 stop
for i in iter1:
    print('one :',i)
    
for i in iter1:         # 실행하기 위해서는  새로운 반복자생성
    print('two : ' ,i)
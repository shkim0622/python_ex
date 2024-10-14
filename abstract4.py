from abc import *

class phone:
    phone_name = "red"
    
    def __init__(self, my_number, my_name):
        self.my_number= my_number
        self.my_name=my_name
        
    def call(self, number):
        print('phone call : {}'.format(number))
        
    def send_msg(self,number,msg):
        print('Phone send : {},{}'.format(number,msg))
        
    def get_info(self):
        print('Phone my number : '.format(self.my_number))
        print('Phone my name : '.format(self.my_name))
        
class childphone(phone):
    def __init__(self, my_number, my_name):
        super().__init__(my_number,my_name)
        print('childphone 생성자 호출')
        
    def button_home(self):
        print('childphone 홈 버튼 누름')

class child2phone(phone):
    def __init__(self, my_number, my_name):
        super().__init__(my_number, my_name)
        print('child2phone 생성자 호출')
    
    def button_cancel(self):
        print('child2phone 취소 버튼 누름')

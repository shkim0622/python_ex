import time

class MyContextManager:
    def __enter__(self):
        print("시작 context")
        time.sleep(3)
        return 100
    
    def __exit__(self, exc_type, exc_value, traceback):
        print("종료 context")

with MyContextManager() as value:
    print(" context ")
    print("Value:", value)

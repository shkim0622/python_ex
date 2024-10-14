from abc import ABC, abstractmethod

class Worker(ABC):
    @abstractmethod
    def work(self):
        pass

class MyCallableContextManager:
    def __init__(self, worker):
        self.worker = worker

    def __enter__(self):
        print("Entering context")
        return self.worker

    def __exit__(self, exc_type, exc_value, traceback):
        print("Exiting context")
        if exc_type:
            print(f"Exception: {exc_type}, {exc_value}, {traceback}")

    def __call__(self):
        print("Calling worker")
        self.worker.work()

class Programmer(Worker):
    def work(self):
        print("Programming")

# 사용 예제
programmer = Programmer()
with MyCallableContextManager(programmer) as callable_worker:
    callable_worker()

# 예외 발생을 시뮬레이션하기 위해 work 메서드를 호출할 때 예외를 발생시킴
class ErrorWorker(Worker):
    def work(self):
        print("Working")
        raise ValueError("Something went wrong")

error_worker = ErrorWorker()
with MyCallableContextManager(error_worker) as callable_worker:
    callable_worker()

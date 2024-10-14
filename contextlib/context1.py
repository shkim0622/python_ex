import contextlib
import time

@contextlib.contextmanager
def context_manager():
    print("시작 context")
    time.sleep(3)
    yield 100
    print("종료 context")
    
    time.sleep(3)
    yield 1000
    print("종료2 context")

# with context_manager() as value:
value=context_manager()

print(" context ")
print("Value:", value)
time.sleep(10)
print("Value:", value)

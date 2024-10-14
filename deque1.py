from collections import deque

data = [1,2,3,4,5]

d =deque(data)
print(d)

d.append(6)
print(d)

d.appendleft(0)
print(d)

d.pop()
print(d)

d.popleft()
print(d)

d.rotate()
print(d)

d.reverse()
print(d)

d.clear()
print(d)
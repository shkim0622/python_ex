from collections import defaultdict

lists=[(1,'a'),(2,'b'),(3,'c'),(1,'aa')]

a_d = defaultdict(list)
for k,v in lists:
    a_d[k].append(v)
print(a_d)

lists2=[(1,'a'),(2,'b'),(3,'c'),(1,'a')]
a_d =defaultdict(int)
for k, _ in lists2:
    a_d[k]+=1   
print(a_d)
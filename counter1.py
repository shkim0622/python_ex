from collections import Counter

count_list1 = ['a','a','b','c','c']
new_list = ['a','c','d','d']

counter = Counter(count_list1)
print(counter)

counter.update(new_list)
print(counter)
print(counter.most_common(n=2))
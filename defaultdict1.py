from collections import defaultdict

def default_func():
    return 3

def_dic = defaultdict(default_func)

def_dic['a'] = 1
def_dic['b'] = 2

print(def_dic)
print(def_dic['c'])
print(def_dic)
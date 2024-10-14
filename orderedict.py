from collections import OrderedDict

order_dic1 = OrderedDict()

order_dic1['a'] = 1
order_dic1['b'] = 2
order_dic1['c'] = 3

order_dic2 = OrderedDict()
order_dic2['c'] = 3
order_dic2['a'] = 1
order_dic2['b'] = 2
print('------------------------------')
print('order_dic1 : ',order_dic1)
print('order_dic2 : ',order_dic2)
print('------------------------------')
if order_dic1 == order_dic2:
    print('order_dic1 == order_dic2')

else:
    print('order_dic1 != order_dic2')
    
print('------------------------------')
order_dic1.update({'d':4})
print('order_dic1 : ',order_dic1)

print('------------------------------')
print('order_dic1.popitem(last=True) : ' , order_dic1.popitem(last=True))
print('order_dic1 : ', order_dic1)
print('------------------------------')
print('order_dic1.popitem(last=False) : ', order_dic1.popitem(last=False))
print('order_dic1 : ', order_dic1)
print('------------------------------')


import collections.abc

class SomeApplicationClass(collections.abc.Callable):
    pass

def some_method(self,other):
    assert isinstance(other,collections.abc.Iterator)

try:
    some_obj.som_method(another)
    

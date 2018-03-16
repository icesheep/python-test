# -*- coding: utf-8 -*-
from functools import reduce
def prod(L):
    def f(x,y):
        return x*y
    return reduce(f,L)
print(prod([1,3,5,2]))
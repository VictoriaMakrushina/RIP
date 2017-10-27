#!/usr/bin/env python3
from librip.gens import gen_random
from librip.iterators import Unique

data0 = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2]
data1 = gen_random(1, 3, 10)

# Реализация задания 2
data2= ['a', 'A', 'A', 'a', 'C', 'a', 'a', 'b', 'b', 'b', 'b', 'b']

d0 = Unique(data0)
for x in d0:
    print(x, end=', ')
print('\n')
d1 = Unique(list(data1))
for x in d1:
    print(x, end=', ')
print('\n')

d2 = Unique(data2, ignore_case=True)
for x in d2:
    print(x, end=', ')
print('\n')

d3 = Unique(data2)
for x in d3:
    print(x, end=', ')
print('\n')
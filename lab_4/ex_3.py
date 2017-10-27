#!/usr/bin/env python3
import math
data = [4, -30, 100, -100, 123, 1, 0, -1, -4]
# Реализация задания 3
#def sort_mod(items):
#    a = math.fabs(items)
#    return a    

#newdata=sorted(data, key = sort_mod)
#print (newdata)

newdata=sorted(data, key = lambda x: math.fabs(x))
print (newdata)
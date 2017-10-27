#!/usr/bin/env python3

from librip.gens import *

goods = [
    {'title': 'Ковер', 'price': 2000, 'color': 'green'},
    {'title': 'Диван для отдыха', 'price': 5300, 'color': 'black'},
    {'title': 'Стелаж', 'price': 7000, 'color': 'white'},
    {'title': 'Вешалка для одежды', 'price': 800, 'color': 'white'}
]

# Реализация задания 1
def lala():
	a = 5
	print(a)
    
for i in field(goods,'title','price'):
    print (i, end=', ')
print ('\n')
for i in gen_random(1, 4, 6):
        print(i, end=', ')
   
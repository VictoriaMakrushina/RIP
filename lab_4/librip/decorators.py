# Здесь необходимо реализовать декоратор, print_result который принимает на вход функцию,
# вызывает её, печатает в консоль имя функции, печатает результат и возвращает значение
# Если функция вернула список (list), то значения должны выводиться в столбик
# Если функция вернула словарь (dict), то ключи и значения должны выводить в столбик через знак равно
# Пример из ex_4.py:
# @print_re
def func_print(items):
        if type(items) == list:
            for i in items:
                print(i)
        elif type(items) == dict:
            for key in items:
                print('%s = %s' % (key, items[key]))
        else:
            print(items)
        return items    
    
def print_result(your_func):
    def get_arg(*args, **kwargs):
        print(your_func.__name__)
        res = func_print(your_func(*args, **kwargs))
        return res

    return get_arg
# 
# @print_result
# def test_2():
#     return 'iu'
#
# @print_result
# def test_3():
#     return {'a': 1, 'b': 2}
#
# @print_result
# def test_4():
#     return [1, 2]
#
# test_1()
# test_2()
# test_3()
# test_4()
#
# На консоль выведется:
# test_1
# 1
# test_2
# iu
# test_3
# a = 1
# b = 2
# test_4
# 1
# 2

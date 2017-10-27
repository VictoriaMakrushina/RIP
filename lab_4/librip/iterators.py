# Итератор для удаления дубликатов
class Unique(object):
    def __init__(self, items, **kwargs):
        
        
        self.lst = items
        self.ignore_case = False
        if 'ignore_case' in kwargs:
            self.ignore_case = kwargs['ignore_case']
        self.newlst = set()    
        
        # Нужно реализовать конструктор
        # В качестве ключевого аргумента, конструктор должен принимать bool-параметр ignore_case,
        # в зависимости от значения которого будут считаться одинаковые строки в разном регистре
        # Например: ignore_case = True, Aбв и АБВ разные строки
        #           ignore_case = False, Aбв и АБВ одинаковые строки, одна из них удалится
        # По-умолчанию ignore_case = False
        

    def __next__(self):
        # Нужно реализовать __next__    
#        if self.index >= len(self.newlst) - 1:
#            raise StopIteration
        
          for i in self.lst:
             if type(i) != int: 
                if self.ignore_case is True:
                    if i.lower() not in self.newlst:
                        self.newlst.add(i.lower())
                        return i
                elif self.ignore_case is False :
                    if i not in self.newlst:
                        self.newlst.add(i)
                        return i
             else:
                 if i not in self.newlst:
                   self.newlst.add(i)
                   return i
      
          raise StopIteration()   
            
            
            
#        self.index += 1
#        return self.newlst[self.index]

    def __iter__(self):
        return self

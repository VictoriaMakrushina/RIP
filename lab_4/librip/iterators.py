# Итератор для удаления дубликатов
class Unique(object):
    def __init__(self, items, **kwargs):
        
        assert len(items) > 0
        
        ignor_case = False
        
        for key in kwargs:
            ignor_case = kwargs[key]
        self.lst = list(map(str, items))
        
        
#       if ignor_case is False:
#            self.lst.sort(key=lambda x: x.lower())
 #       else:
  #          self.lst.sort()
           
            
        self.newlst = []
        counter = 0
        self.newlst.append(self.lst[0])
#        for i in self.lst:
        if ignor_case is False:
                a=set()
                for i in self.lst:
                   m= self.lst[counter].lower()
                   a.add(m)
                   self.newlst=list(a)
 #               if i.lower() != self.newlst[counter].lower():
 #                  self.newlst.append(i)
                   counter += 1
        elif ignor_case is True:
                a=set(self.lst)
                self.newlst=list(a)
  #              if i != self.newlst[counter]:
  #                  self.newlst.append(i)
  #                  counter += 1

        self.index = -1    
        # Нужно реализовать конструктор
        # В качестве ключевого аргумента, конструктор должен принимать bool-параметр ignore_case,
        # в зависимости от значения которого будут считаться одинаковые строки в разном регистре
        # Например: ignore_case = True, Aбв и АБВ разные строки
        #           ignore_case = False, Aбв и АБВ одинаковые строки, одна из них удалится
        # По-умолчанию ignore_case = False
        

    def __next__(self):
        # Нужно реализовать __next__    
        if self.index >= len(self.newlst) - 1:
            raise StopIteration
        self.index += 1
        return self.newlst[self.index]

    def __iter__(self):
        return self

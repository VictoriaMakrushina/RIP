# Здесь необходимо реализовать
# контекстный менеджер timer
# Он не принимает аргументов, после выполнения блока он должен вывести время выполнения в секундах
# Пример использования
# with timer():
#   sleep(5.5)
#
# После завершения блока должно вывестись в консоль примерно 5.5
import time


class timer:
    def __enter__(self):
        self.start = time.time()
        self.date=self.start
        return self

    def __exit__(self, *args):
        self.end = time.time()
        self.sec = self.end - self.start
        print("with timer(): %s" % self.sec)
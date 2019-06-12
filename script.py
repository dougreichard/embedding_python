from my_api import *
class Cat(Animal):
    def go(self, n_times):
        return "meow! " * n_times
d = Dog()
print(call_go(d))

s = Cat()
print(call_go(s))
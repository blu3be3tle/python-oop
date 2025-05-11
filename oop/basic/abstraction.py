from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass

class Lion(Animal):
    def sound(self):
        return "Rawr"

class Cat(Animal):
    def sound(self):
        return "Meow"

# Abstract class can't be instantiated
# animal = Animal()  ❌
c = Cat()
print(c.sound())  # ✅ Meow

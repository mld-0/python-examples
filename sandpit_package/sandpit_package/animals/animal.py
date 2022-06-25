from abc import ABC, abstractmethod

class Animal(ABC):

    def __init__(self, name):
        self.name = name

    def speak(self):
        speech = self._sound() + ", I am " + self.name
        print(speech)

    @abstractmethod
    def _sound(self):
        ...

    @abstractmethod
    def walk(self):
        ...


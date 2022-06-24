from animals.animal import Animal

class Cat(Animal):

    def _sound(self):
        return "mew"

    def walk(self):
        print("*adorable stalking intensifies*")


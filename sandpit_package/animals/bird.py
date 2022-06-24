from animals.animal import Animal

class Bird(Animal):

    def _sound(self):
        return "chirp"

    def walk(self):
        print("*swoop*")


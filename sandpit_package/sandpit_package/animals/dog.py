from sandpit_package.animals.animal import Animal

class Dog(Animal):
    
    def _sound(self):
        return "ruf"

    def walk(self):
        print("*this is the most fun ever*")


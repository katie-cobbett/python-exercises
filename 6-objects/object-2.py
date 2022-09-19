
from random import randint, randrange
# This is about inheritance. The monkey class can inherit stuff from its parents class. 


class Animal:
    def __init__(self,name):
        self.name = name
        self.hunger = randrange(2,10)

    def __str__(self):
        return str(self.__dict__)

    def is_hungry(self) -> bool:
        if self.hunger > 5:
            return True
        else:
            return False

class Mammal(Animal):
    def __init__(self,name):
        super().__init__(name)

# The class monkey does everything that animal does, but monkey is an animal. B
# but i is a monkey type of animal. 
# all things  that you can do to animal, can do to monkey. not all things you ca do 
# To monkey, you can do to animal. 
class Monkey(Mammal):
    def __init__(self,name,fur_length:int):
        super().__init__(name)
        self.fur_length = fur_length
        
    def swing(self) -> str:
        return "yay"

# creating an object of the class animal.
generic_animal = Animal(name="george")
# generic_animal.swing() - invalid.
my_monkey = Monkey(name= "shaggybaboonirooni", fur_length=99)
response = my_monkey.swing()
print(response)

print("is my_monkey hungry? {}".format(my_monkey.is_hungry() ))


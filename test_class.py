class Animal:
    legs = 4
    eyes = 2


class Dog(Animal):
    sound = 'Bark'

    def __init__(self,name):
        self.name = name

    def __str__(self):
        return self.name

myDog = Dog('Lassy')
print(myDog)
print(myDog.legs)
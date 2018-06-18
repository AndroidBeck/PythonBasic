__author__ = 'Evdokimov'
class Dog:
    legs = 4
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def bark(self):
        print("Woof!")

fido = Dog("Fido", "brown")
print(fido.name)
fido.bark()
print(Dog.legs)
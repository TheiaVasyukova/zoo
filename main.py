class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        pass

    def eat(self):
        print(f"{self.name} кушает")

class Bird(Animal):
    def __init__(self, name, age, wings):
        super().__init__(name, age)
        self.wings = wings

    def make_sound(self):
        print(f"{self.name} щебечет")

class Mammal(Animal):
    def __init__(self, name, age, fur_color):
        super().__init__(name, age)
        self.fur_color = fur_color

    def make_sound(self):
        print(f"{self.name} рычит")

class Reptile(Animal):
    def __init__(self, name, age, type):
        super().__init__(name, age)
        self.type = type

    def make_sound(self):
        print(f"{self.name} шипит")


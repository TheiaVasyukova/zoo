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

def animal_sound(animals):
    for animal in animals:
        animal.make_sound()

animals = [
    Bird("Дрозд", 2, "небольшие крылья"),
    Mammal("Тигр", 5, "белый с полосками"),
    Reptile("Змея", 3, "ядовитая")
]

animal_sound(animals)

class Zoo:
    def __init__(self):
        self.animals = []
        self.staff = []

    def add_animal(self, animal):
        self.animals.append(animal)

    def add_staff(self, staff):
        self.staff.append(staff)

    def show_animals(self):
        for animal in self.animals:
            print(f"{animal.name}, возраст: {animal.age}")

    def show_staff(self):
        for member in self.staff:
            print(f"{member.name}, должность: {member.role}")

zoo = Zoo()
zoo.add_animal(Bird("Коршун", 4, "средние крылья"))
zoo.add_animal(Mammal("Мартышка", 3, "серый"))
zoo.show_animals()

class Staff:
    def __init__(self, name, role):
        self.name = name
        self.role = role

class ZooKeeper(Staff):
    def __init__(self, name):
        super().__init__(name, "Смотритель")

    def feed_animal(self, animal):
        print(f"{self.name} кормит {animal.name}.")

class Veterinarian(Staff):
    def __init__(self, name):
        super().__init__(name, "Ветеринар")

    def heal_animal(self, animal):
        print(f"{self.name} лечит {animal.name}.")

zoo_keeper = ZooKeeper("Иванов Иван Петрович")
vet = Veterinarian("Сидоров Илья Прокофьевич")

zoo.add_staff(zoo_keeper)
zoo.add_staff(vet)
zoo.show_staff()

zoo_keeper.feed_animal(animals[0])
vet.heal_animal(animals[1])



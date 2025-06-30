# Создание базового класса "Животное" и его наследование для создания классов
# "Собака" и "Кошка". В классе "Животное" будут общие методы, такие как "дышать"
# и "питаться", а классы-наследники будут иметь свои уникальные методы и свойства,
# такие как "гавкать" и "мурлыкать". 

class Animal:
    def __init__(self, name):
        self.name = name

    def breathe(self):
        print(f"{self.name} дышит.")

    def eat(self):
        print(f"{self.name} ест.")

class Dog(Animal):
    def bark(self):
        print(f"{self.name} гавкает!")

class Cat(Animal):
    def purr(self):
        print(f"{self.name} мурлычет.")

if __name__ == "__main__":
    # Создаем экземпляры классов
    dog = Dog("Шарик")
    cat = Cat("Мурка")
    
    dog.breathe()
    dog.eat()
    dog.bark()

    cat.breathe()
    cat.eat()
    cat.purr()

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

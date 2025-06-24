# Создайте класс "Человек" с атрибутами "имя", "возраст" и "пол". Напишите метод,
# который выводит информацию о человеке в формате "Имя: имя, Возраст: возраст,
# Пол: пол".


class Person:
    def __init__(self, name, age, gender):
        self.name = name  # Имя
        self.age = age    # Возраст
        self.gender = gender  # Пол

    def display_info(self):
        """Метод для вывода информации о человеке."""
        print(f"Имя: {self.name}, Возраст: {self.age}, Пол: {self.gender}")

# Пример использования класса
if __name__ == "__main__":
    # Создаем экземпляр класса Person
    person1 = Person("Алексей", 30, "Мужской")
    person2 = Person("Мария", 25, "Женский")

    # Выводим информацию о человеке
    person1.display_info()
    person2.display_info()

# Для задачи из блока 1 создать две функции, save_def и load_def, которые позволяют
# сохранять информацию из экземпляров класса (3 шт.) в файл и загружать ее обратно.
# Использовать модуль pickle для сериализации и десериализации объектов Python в
# бинарном формате.

import pickle

class Person:
    def __init__(self, name, age, gender):
        self.name = name  # Имя
        self.age = age    # Возраст
        self.gender = gender  # Пол

    def display_info(self):
        """Метод для вывода информации о человеке."""
        print(f"Имя: {self.name}, Возраст: {self.age}, Пол: {self.gender}")

def save_def(people, filename):
    """Сохраняет список объектов Person в файл."""
    with open(filename, 'wb') as f:
        pickle.dump(people, f)

def load_def(filename):
    """Загружает список объектов Person из файла."""
    with open(filename, 'rb') as f:
        return pickle.load(f)

# Пример использования
if __name__ == "__main__":
    # Создаем экземпляры класса Person
    person1 = Person("Алексей", 30, "Мужской")
    person2 = Person("Мария", 25, "Женский")
    person3 = Person("Иван", 40, "Мужской")

    # Список людей
    people = [person1, person2, person3]

    # Сохраняем информацию в файл
    save_def(people, 'people.pkl')
    print("Информация о людях сохранена в файл 'people.pkl'.")

    # Загружаем информацию из файла
    loaded_people = load_def('people.pkl')
    print("Информация о людях загружена из файла:")

    for person in loaded_people:
        person.display_info()

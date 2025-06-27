# В исходном текстовом файле(Dostoevsky.txt) найти все произведения писателя.
# Посчитать количество полученных элементов.

import re
p = re.compile('«([а-яА-Я\s]+)»')

def find_works_in_file(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        content = file.read()

    # Предположим, что произведения разделены строками, начинающимися с "Название:"
    # Замените этот шаблон на тот, который соответствует вашему файлу
    works = p.findall(content)

    # убираем повторения
    works = list(set(works))

    # Удаляем пустые строки и пробелы
    works = [work.strip() for work in works if work.strip()]

    return works

# Пример использования
input_filename = 'Dostoevsky.txt'
works = find_works_in_file(input_filename)

# Выводим результаты
print(f"Найдено произведений: {len(works)}")
for i, work in enumerate(works, start=1):
    print(f"{i}. {work[:30]}...")  # Выводим первые 30 символов каждого произведения

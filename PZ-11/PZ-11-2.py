# Из предложенного текстового файла (text18-8.txt) вывести на экран его содержимое,
# количество символов, принадлежащих к группе букв. Сформировать новый файл, в
# который поместить текст в стихотворной форме предварительно удалив букву «с» из
# текста.


def process_file(input_filename, output_filename):
    with open(input_filename, 'r', encoding='utf-8') as f:
        text = f.read()

    # Подсчет количества букв
    letter_count = sum(1 for char in text if char.isalpha())

    # Удаление буквы 'с' из текста
    modified_text = text.replace('с', '').replace('С', '')

    # Запись результата в новый файл
    with open(output_filename, 'w', encoding='utf-8') as f:
        f.write(modified_text)

    return letter_count

input_filename = 'text18-8.txt'  # Исходный файл
output_filename = 'modified_text.txt'  # Новый файл

letter_count = process_file(input_filename, output_filename)

print(f"Содержимое файла '{input_filename}' обработано.")
print(f"Количество букв в файле: {letter_count}")
print(f"Результат записан в файл '{output_filename}'.")

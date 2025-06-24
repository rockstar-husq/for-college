# Составить генератор (yield), который преобразует все буквенные символы в
# заглавные.

def uppercase_generator(s):
    for char in s:
        if char.isalpha():  # Проверяем, является ли символ буквой
            yield char.upper()
        else:
            yield char  # Если не буква, возвращаем символ как есть

# Пример использования
input_string = "Hello, World!"
uppercase_gen = uppercase_generator(input_string)

# Печатаем результат
result = ''.join(uppercase_gen)
print("Результат:", result)

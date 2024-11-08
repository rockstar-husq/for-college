# Даны два целых числа: A, B. Проверить истинность высказывания: «Каждое из чисел
# A и B нечетное».

# Введем 2 переменные 
try:
    Number_A = int(input('Input number A: '))
    Number_B = int(input('Input number B: '))

    # Введем переменную для нахождения нечетности
    Division_2 = Number_A % 2
    Division_22 = Number_B % 2

    # Проверяем нечетность
    if Division_2 == 1:
        if Division_22 == 1:
            print('True! Числа ',Number_A,' и ',Number_B,' - нечетные!')
        else:
            print('False! Одно или оба числа - Четные!')
    else:
        print('False! Одно или оба числа - Четные!')

# Добавим защиту от ошибок если пользователь ввел неккоректное значение
except ValueError:
    print('Введите числовое значение! Без точек и запятых.')

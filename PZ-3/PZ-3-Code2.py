# Единицы длины пронумерованы следующим образом: 1 — дециметр, 2 — километр,
# 3 — метр, 4 — миллиметр, 5 — сантиметр. Дан номер единицы длины (целое число
# в диапазоне 1-5) и длина отрезка в этих единицах (вещественное число). Найти
# длину отрезка в метрах.

# Введем некоторые переменные в миллиметрах
One = 100
Two = 1000000
Three = 1000
Four = 1
Five = 10

# Обозначим номера единиц длины
print('1 — дециметр, 2 — километр, 3 — метр, 4 — миллиметр, 5 — сантиметр.')

# Введем переменную, которая обозначает номер единицы длины
try:
    Number = int(input('Введите номер (1-5): '))
    if Number <= 0 or Number >= 6:
        print('Введите число от 1 до 5!')
        exit()

    # Введем переменную длины
    Long = int(input('Введите длину: '))

    # Расчитаем длину отрезка
    if Number == 1:
        Total_long = One * Long
        Total_long = Total_long / 1000
        print('Длина отрезка в метрах составляет', Total_long, ' метров')

    elif Number == 2:
        Total_long = Two * Long
        Total_long = Total_long / 1000
        print('Длина отрезка в метрах составляет', Total_long, ' метров')

    elif Number == 3:
        Total_long = Three * Long
        Total_long = Total_long / 1000
        print('Длина отрезка в метрах составляет', Total_long, ' метров')

    elif Number == 4:
        Total_long = Four * Long
        Total_long = Total_long / 1000
        print('Длина отрезка в метрах составляет', Total_long, ' метров')

    elif Number == 5:
        Total_long = Five * Long
        Total_long = Total_long / 1000
        print('Длина отрезка в метрах составляет', Total_long, ' метров')

# Добавим защиту от ошибок если пользователь ввел неккоректное значение
except ValueError:
    print('Введите числовое значение! Без точек и запятых.')
# Даны два целых числа A и B (A < B). Найти сумму квадратов всех целых чисел от A
# до B включительно.

print('Даны два целых числа A и B (A < B). Найти сумму квадратов всех целых чисел')
print('от A до B включительно.')

# Введем обработку исключений
try:
    num_a = int(input('Input A number: '))
    num_b = int(input('Input B number: '))
    tsum = 0

    # Введем условие проверки чисел
    if num_a > num_b:
        print('Некоректные значения!')
    else:

        # Введем цикл while который будет расчитывать сумму всех квадратов
        while num_a <= num_b :
            psum = num_a ** 2
            num_a = num_a + 1
            tsum += psum
        print('total sum is : ', tsum)
except ValueError:
    print('Введите целое числовое значение!')

# Описать функцию AddLeftDigit(D, K), добавляющую к целому положительному
# числу K слева цифру D (D — входной параметр целого типа, лежащий в диапазоне
# 1-9, K — параметр целого типа, являющийся одновременно входным и выходным).
# С помощью этой функции последовательно добавить к данному числу K слева
# данные цифры D1 и D2, выводя результат каждого добавления.

# Введем функцию с 2 переменными
def AddLeftDigit(d, k):
    if 1 <= d <= 9:
        k = int(str(d) + str(k))
    else:
        print('input number in range 1-9!')
    return k

# Обработка исключений
try:
    k = int(input('Input k number: '))
    d1 = int(input('Input d1 number in range 1-9 : '))
    d2 = int(input('Input d2 number in range 1-9 : '))

    # Введем переменную для сохранения k
    f = k

    # Вызываем функцию с переменной k
    k = AddLeftDigit(d1, k)
    print('Result addition 1 : ', k)

    k = f
    k = AddLeftDigit(d2, k)
    print('Result addition 2 : ', k)

except ValueError:
    print('Input integer data!')
# Дано целое число N (>0) и символ C. Вывести строку длины N, которая состоит из
# символов C.

# введем пустой лист
listo = []

# введем переменные для длины и символа
try:
    long = int(input('Input list lenght: '))
    symbol = input('Input any symbol: ')

    # цикл добавляющий нужное количество символов
    t = 0
    while t < long:
        if len(symbol) == 1:
            listo.append(symbol)
            t += 1
        else:
            print('input symbol (1)')
            break

    # переводим список в строку
    neu_string = ''.join(listo)

    # print(type(neu_string))
    # выводим результат
    print(neu_string)

except ValueError:
    print('Input correct data!')
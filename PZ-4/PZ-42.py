# Начальный вклад в банке равен 1000 руб. Через каждый месяц размер вклада
# увеличивается на P процентов от имеющейся суммы (P — вещественное число, 0< P
# <25). По данному P определить, через сколько месяцев размер вклада превысит 1100
# руб., и вывести найденное количество месяцев K (целое число) и итоговый размер
# вклада S (вещественное число).

vklad = 1000
months = 0
try:
    num_p = int(input('Input number in range 0-25 : '))
    if num_p > 25 or num_p < 0:
        print('Input number in range!')
    else:
        while vklad < 1100:
            vklad = vklad + (vklad * (num_p / 100))
            months = months + 1
        print('Time in monthses : ', months,', total vklad : ', vklad)
except ValueError:
    print('Input INT format!')
# Даны два целых числа A и B (A < B). Найти сумму квадратов всех целых чисел от A
# до B включительно.

print('Даны два целых числа A и B (A < B). Найти сумму квадратов всех целых чисел')
print('от A до B включительно.')
try:
    num_a = int(input('Input first number: '))
    num_b = int(input('Input second number: '))
    if num_a > num_b:
        print('Некоректные значения!')
    while num_a != (num_b):
        psum = 0
        psum = psum + (num_a * num_a)
        num_a = num_a + 1
        total_sum = 0
        total_sum = total_sum + psum
    print('total sum is : ', total_sum)
except ValueError:
    print('Введите целое числовое значение!')
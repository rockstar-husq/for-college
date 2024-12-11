# Составить программу, в которой функцию построит изображение, в котором в
# первой строке 1 звездочка, во второй - 2, в третьей -3, ..., в строке с номером m - m
# звездочек.

# Введем функцию stars с переменной m
def stars(m):
    for i in range(1, m + 1):
        print('*'*i)

# Обработка исключений
try:
    # Введем вызов функции и переменную для количества строк
    num_line = int(input('Input number of strings : '))
    stars(num_line)
except ValueError:
    print('Input integer data!')
# В двумерном списке элементы столбца N (N задать с клавиатуры) увеличить в два
# раза.

def increase_column_by_two(matrix, column_index):
    for row in matrix:
        if column_index < len(row):  # Проверяем, что индекс столбца корректен
            row[column_index] *= 2

# Пример использования
rows = int(input("Введите количество строк: "))
cols = int(input("Введите количество столбцов: "))
matrix = []

# Заполнение двумерного списка
for i in range(rows):
    row = list(map(int, input(f"Введите элементы строки {i + 1} через пробел: ").split()))
    matrix.append(row)

# Запрос индекса столбца
n = int(input("Введите индекс столбца для увеличения (0 - основание): "))

# Увеличиваем элементы столбца N в два раза
increase_column_by_two(matrix, n)

# Вывод результата
print("Обновленная матрица:")
for row in matrix:
    print(row)

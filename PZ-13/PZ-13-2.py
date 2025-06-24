 # В двумерном списке элементы последней строки заменить на 0.

def replace_last_row_with_zero(matrix):
    if matrix:  # Проверяем, что матрица не пустая
        matrix[-1] = [0] * len(matrix[-1])  # Заменяем последнюю строку на нули

# Пример использования
rows = int(input("Введите количество строк: "))
cols = int(input("Введите количество столбцов: "))
matrix = []

# Заполнение двумерного списка
for i in range(rows):
    row = list(map(int, input(f"Введите элементы строки {i + 1} через пробел: ").split()))
    matrix.append(row)

# Заменяем элементы последней строки на 0
replace_last_row_with_zero(matrix)

# Вывод результата
print("Обновленная матрица:")
for row in matrix:
    print(row)

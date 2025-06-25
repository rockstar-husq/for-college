# Средствами языка Python сформировать текстовый файл (.txt), содержащий
# последовательность из целых положительных и отрицательных чисел. Сформировать
# новый текстовый файл (.txt) следующего вида, предварительно выполнив требуемую
# обработку элементов:
# Исходные данные:
# Количество элементов:
# Индекс последнего минимального элемента:
# Сумма элементов больших 10 во второй половине: 

def process_numbers(input_filename, output_filename):
    with open(input_filename, 'r') as f:
        numbers = list(map(int, f.read().strip().split()))

    # Исходные данные
    count_elements = len(numbers)

    # Индекс последнего минимального элемента
    if numbers:
        min_value = min(numbers)
        last_min_index = len(numbers) - 1 - numbers[::-1].index(min_value)
    else:
        last_min_index = -1  # Если список пустой

    # Сумма элементов больше 10 во второй половине
    second_half = numbers[count_elements // 2:]
    sum_greater_than_10 = sum(x for x in second_half if x > 10)

    # Запись результатов в новый файл
    with open(output_filename, 'w') as f:
        f.write(f"Исходные данные: {numbers}\n")
        f.write(f"Количество элементов: {count_elements}\n")
        f.write(f"Индекс последнего минимального элемента: {last_min_index}\n")
        f.write(f"Сумма элементов больших 10 во второй половине: {sum_greater_than_10}\n")

# Пример использования
output_filename = 'output_results.txt'
process_numbers(input_filename, output_filename)
print(f"Результаты записаны в файл '{output_filename}'.")

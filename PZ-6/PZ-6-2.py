# Дан список размера N. Найти количество участков, на которых его элементы
# монотонно возрастают.

# введем функцию
def count_segment(lean):
    if len(lean) == 0:
        return 0
    
    count = -1
    increase = False

    # введем цикл для подсчета участков
    for i in range(1, len(lean)):
        if lean[i] > lean[i-1]:
            if not increase:
                count += 1
                increase = True

            else:
                increase = False

    return count

# обработка исключений
try:
    N = int(input("Input size : "))
    lean = [int(input(f"input element {i + 1} : ")) for i in range(N)]
    result = count_segment(lean)
    print("Count of increasing segment : ", result)

except ValueError:
    print("Input integer data!")
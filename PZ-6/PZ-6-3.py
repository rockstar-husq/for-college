# Дан список размера N. Заменить каждый элемент списка на среднее арифметическое
# этого элемента и его соседей.

# вводим функцию
def replace_el(lean):
    if len(lean) == 0:
        return lean
    
    # новый список для результатов работы цикла
    new_lean = []
    n = len(lean)

    for i in range(n):
        if i == 0:
            # для первого значения
            element = (lean[i] + lean[i + 1]) / 2
        
        elif i == n - 1:
            # для последнего значения
            element = (lean[i] + lean[i - 1]) / 2

        else:
            # для средних значений
            element = (lean[i - 1] + lean[i] + lean[i + 1]) / 3

        new_lean.append(element)

    return new_lean

# обработка исключений
try:
    N = int(input("Input size : "))
    lean = [int(input(f"Input element {i + 1} : ")) for i in range(N)]

    new_lean = replace_el(lean)
    print("New list : ", new_lean)

except ValueError:
    print("input integer data!")
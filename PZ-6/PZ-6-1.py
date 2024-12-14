# Дан целочисленный список размера 10. Вывести все содержащиеся в данном списе
# четные числа в порядке убывания их индексов, а также их количество K.

# Вводим функцию для подсчета четных чисел
def chetnue_numbers(numbers):
    num_list = []

    for index in range(len(numbers) -1, -1, -1):
        if numbers[index] % 2 == 0:
            num_list.append(numbers[index])
    
    return num_list

# Обработка исключений
try:
    numbers = [int(input(f"Input element {i + 1} (number) : ")) for i in range(10)]

    num_list = chetnue_numbers(numbers)
    K = len(num_list)

    print("Chet numbers in negative index upscale : ", num_list)
    print("Count of chet numbers : ", K)

except ValueError:
    print("Input integer number!")
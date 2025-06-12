# Дана строка 'апельсины 45 991 63 100 12 яблоки 13 47 26 0 16',
# отражающая продажи продукции по дням в кг. Преобразовать информацию из
# строки в словари, с использованием функции найти среднее значение продаж по
# каждому виду продукции, результаты вывести на экран.

# создадим строку в которую запишем данные
info = 'апельсины 45 991 63 100 12 яблоки 13 47 26 0 16'

def delim():
    # разделяем строку на части
    info_list = info.split()

    # создаем словари для хранения данных
    sales_data = {}

    current_fruit = None

    for item in info_list:
        if item.isalpha():  # если это название фрукта
            current_fruit = item
            sales_data[current_fruit] = {'sales': []}  # инициализируем список продаж
        else:  # если это число
            if current_fruit:  # проверяем, что фрукт уже установлен
                sales_data[current_fruit]['sales'].append(int(item))  # добавляем продажи

    # вычисляем среднее значение продаж для каждого фрукта
    average_sales = {}
    for fruit, data in sales_data.items():
        average_sales[fruit] = sum(data['sales']) / len(data['sales'])

    # выводим результаты
    for fruit, avg in average_sales.items():
        print(f'Среднее значение продаж для {fruit}: {avg:.2f} кг')

delim()

# Приложение ЗАКАЗЫ ТОВАРОВ для автоматизированного контроля заказов
# торговой фирмы. Таблица Заказы должна содержать информацию о товарах со
# следующей структурой записи: Код товара, Наименование товара, Заказчик
# (наименование организации, возможны повторяющиеся значения), Дата заказа, Срок
# исполнения (от 1 до 10 дней), Стоимость заказа. 

import sqlite3

# Создание или подключение к базе данных
conn = sqlite3.connect('orders.db')
cursor = conn.cursor()

# Создание таблицы Заказы
cursor.execute('''
CREATE TABLE IF NOT EXISTS Orders (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_code TEXT NOT NULL,
    product_name TEXT NOT NULL,
    customer_name TEXT NOT NULL,
    order_date TEXT NOT NULL,
    delivery_time INTEGER NOT NULL CHECK(delivery_time BETWEEN 1 AND 10),
    order_cost REAL NOT NULL
)
''')

conn.commit()

def add_order(product_code, product_name, customer_name, order_date, delivery_time, order_cost):
    cursor.execute('''
    INSERT INTO Orders (product_code, product_name, customer_name, order_date, delivery_time, order_cost)
    VALUES (?, ?, ?, ?, ?, ?)
    ''', (product_code, product_name, customer_name, order_date, delivery_time, order_cost))
    conn.commit()

def view_orders():
    cursor.execute('SELECT * FROM Orders')
    orders = cursor.fetchall()
    for order in orders:
        print(order)

def delete_order(order_id):
    cursor.execute('DELETE FROM Orders WHERE id = ?', (order_id,))
    conn.commit()
  
def main():
    while True:
        print("\nМеню:")
        print("1. Добавить заказ")
        print("2. Просмотреть заказы")
        print("3. Удалить заказ")
        print("4. Выход")

        choice = input("Выберите действие: ")

        if choice == '1':
            product_code = input("Введите код товара: ")
            product_name = input("Введите наименование товара: ")
            customer_name = input("Введите наименование заказчика: ")
            order_date = input("Введите дату заказа (YYYY-MM-DD): ")
            delivery_time = int(input("Введите срок исполнения (от 1 до 10 дней): "))
            order_cost = float(input("Введите стоимость заказа: "))
            add_order(product_code, product_name, customer_name, order_date, delivery_time, order_cost)
            print("Заказ добавлен.")

        elif choice == '2':
            print("Список заказов:")
            view_orders()

        elif choice == '3':
            order_id = int(input("Введите ID заказа для удаления: "))
            delete_order(order_id)
            print("Заказ удален.")

        elif choice == '4':
            break

        else:
            print("Неверный выбор. Пожалуйста, попробуйте снова.")

if __name__ == "__main__":
    main()

conn.close()

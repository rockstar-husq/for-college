import tkinter as tk
from tkinter import messagebox
def calculate_price():
    try:
        kg = float(entry_kg.get())  # Количество килограммов конфет
        price = float(entry_price.get())  # Стоимость ? кг конфет
        current = float(entry_y.get())  # Количество килограммов для расчета
        price_per_kg = price / kg  # Стоимость 1 кг конфет
        total_price = price_per_kg * current  # Стоимость ? кг конфет
        messagebox.showinfo("Результат", f"Стоимость 1 кг конфет: {price_per_kg:.2f} рублей\n" f"Стоимость {current} кг конфет: {total_price:.2f} рублей")
    except ValueError:
        messagebox.showerror("Ошибка", "Пожалуйста, введите корректные числовые значения.")

# Создание основного окна
root = tk.Tk()
root.title("Калькулятор стоимости конфет")

# Ввод данных
label_kg = tk.Label(root, text="Введите количество кг конфет:")
label_kg.pack()
entry_kg = tk.Entry(root)
entry_kg.pack()

label_price = tk.Label(root, text="Введите стоимость этих кг конфет:")
label_price.pack()
entry_price = tk.Entry(root)
entry_price.pack()

label_y = tk.Label(root, text="Введите количество кг для расчета:")
label_y.pack()
entry_y = tk.Entry(root)
entry_y.pack()

# Кнопка для расчета
button_calculate = tk.Button(root, text="Рассчитать", command=calculate_price)
button_calculate.pack()

# Запуск основного цикла приложения
root.mainloop()

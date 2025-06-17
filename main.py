import tkinter as tk
import mysql.connector as mysql

from constants import MAIN_BG_COLOR, SECONDARY_BG_COLOR, FONT, FOCUS_BG
from PIL import Image

# подключение к базе
db = mysql.connect(
    host = "localhost",
    user = "root",
    passwd = "toor",
    database = "zub"
)

# получение массива данных с таблиц
cursor = db.cursor()
cursor.execute("SELECT * FROM materials")
materials_data = cursor.fetchall()
cursor.execute("SELECT * FROM products")
products_data = cursor.fetchall()
cursor.execute("SELECT * FROM suppliers")
suppliers_data = cursor.fetchall()
cursor.close()
db.close()

# функция удаления материала по кнопке
def delete_material(id):
    cursor = db.cursor()
    query = "DELETE FROM materials WHERE id = %s"
    cursor.execute(query, (id))
    cursor.close()
    db.close()
    print(f"Поставщик с ID {id} удален")

# Окно материалов
def open_materials():
    new_window = tk.Toplevel()
    new_window.title("Материалы")
    new_window.geometry("1000x800")
    label = tk.Label(new_window, text="Список материалов", font=(FONT, 10), bg=FOCUS_BG)
    label.pack(pady=20)
    print(materials_data)
    if not materials_data:
        print("Нет данных или ошибка подключения к БД")
        return
    else:
        # Вывод всех материалов плюс присвоение для каждого пля label
        for material in materials_data:
            label_type = tk.Label(new_window, text=f"Тип: {material[1]}", font=(FONT, 10), bg=SECONDARY_BG_COLOR)
            label_type.pack(pady=5)
            label_name = tk.Label(new_window, text=f"Наименование: {material[2]}", font=(FONT, 10), bg=SECONDARY_BG_COLOR)
            label_name.pack(pady=5)
            label_min = tk.Label(new_window, text=f"Минимальное количество: {material[8]}", font=(FONT, 10), bg=SECONDARY_BG_COLOR)
            label_min.pack(pady=5)
            label_price = tk.Label(new_window, text=f"Цена: {material[5]}", font=(FONT, 10), bg=SECONDARY_BG_COLOR)
            label_price.pack(pady=5)
            delete_button = tk.Button(new_window, text="Удалить", command=lambda id=material[0]: delete_material(id), bg=FOCUS_BG)
            delete_button.pack(pady=5)

# Окно продуктов
def open_products():
    new_window = tk.Toplevel()
    new_window.title("Продукты")
    new_window.geometry("1000x800")
    label = tk.Label(new_window, text="Список продуктов", font=(FONT, 10), bg=FOCUS_BG)
    label.pack(pady=20)
    print(products_data)
    if not products_data:
        print("Нет данных или ошибка подключения к БД")
        return
    else:
        for product in products_data:
            label_type = tk.Label(new_window, text=f"Тип: {product[1]}", font=(FONT, 10), bg=SECONDARY_BG_COLOR)
            label_type.pack(pady=5)
            label_name = tk.Label(new_window, text=f"Наименование: {product[2]}", font=(FONT, 10), bg=SECONDARY_BG_COLOR)
            label_name.pack(pady=5)


# Окно поставщиков
def open_suppliers():
    new_window = tk.Toplevel()
    new_window.title("Поставщики")
    new_window.geometry("1000x800")
    label = tk.Label(new_window, text="Список поставщков", font=(FONT, 10), bg=FOCUS_BG)
    label.pack(pady=20)
    print(suppliers_data)
    if not suppliers_data:
        print("Нет данных или ошибка подключения к БД")
        return
    else:
        for supplier in suppliers_data:
            label_type = tk.Label(new_window, text=f"Тип: {supplier[1]}", font=(FONT, 10), bg=SECONDARY_BG_COLOR)
            label_type.pack(pady=5)
            label_name = tk.Label(new_window, text=f"Наименование: {supplier[2]}", font=(FONT, 10), bg=SECONDARY_BG_COLOR)
            label_name.pack(pady=5)

if __name__ == '__main__':
    try:
        root = tk.Tk()
        root.title("Мозаика")
        root.iconbitmap('image/Мозаика.ico')
        root.geometry("850x500")
        root.configure(bg=MAIN_BG_COLOR)

        logo_img = Image.open("image/Мозаика.png")
        logo_img.thumbnail((100, 100))

        def button1_click():
            open_materials()

        def button2_click():
            open_products()

        def button3_click():
            open_suppliers()

        button1 = tk.Button(root, text="Материалы", command=button1_click)
        button2 = tk.Button(root, text="Продукты", command=button2_click)
        button3 = tk.Button(root, text="Поставщики", command=button3_click)
        button1.place(relx=0.5, rely=0.3, anchor=tk.CENTER)
        button2.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        button3.place(relx=0.5, rely=0.7, anchor=tk.CENTER)

        root.mainloop()
    except Exception as e:
        print("Глобальная ошибка:", e)
        input("Нажмите Enter для выхода...")

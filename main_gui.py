import dearpygui.dearpygui as dpg
from Task_1.Client import Client
from Task_2.Vehicle import Vehicle
from Task_3.Train import train
from Task_3.Airplane import Airplane
from Task_3.TransportCompany import TransportCompany

company = TransportCompany("ЛогистикПро")

# === Вспомогательные функции ===
def show_about():
    dpg.configure_item("about_window", show=True)

def add_client_callback(sender, app_data, user_data):
    name = dpg.get_value("client_name")
    weight = dpg.get_value("client_weight")
    vip = dpg.get_value("client_vip")

    if not name.isalpha() or len(name) < 2:
        dpg.configure_item("status_bar", default_value="Ошибка: имя должно содержать только буквы и минимум 2 символа")
        return
    if weight <= 0 or weight > 10000:
        dpg.configure_item("status_bar", default_value="Ошибка: вес должен быть от 1 до 10000 кг")
        return

    client = Client(name, weight, vip)
    company.add_client(client)

    # Добавляем строку в таблицу клиентов
    with dpg.table_row(parent="clients_table"):
        dpg.add_text(client.name)
        dpg.add_text(str(client.cargo_weight))
        dpg.add_text("VIP" if client.is_vip else "Обычный")

    dpg.configure_item("status_bar", default_value="Клиент добавлен")



def add_vehicle_callback(sender, app_data, user_data):
    vtype = dpg.get_value("vehicle_type")
    capacity = dpg.get_value("vehicle_capacity")

    if capacity <= 0:
        dpg.configure_item("status_bar", default_value="Ошибка: грузоподъёмность должна быть > 0")
        return

    if vtype == "Грузовик":
        vehicle = Vehicle(capacity)
    elif vtype == "Поезд":
        cars = dpg.get_value("train_cars")
        vehicle = train(capacity, cars)
    elif vtype == "Самолёт":
        alt = dpg.get_value("airplane_altitude")
        vehicle = Airplane(capacity, alt)
    else:
        dpg.configure_item("status_bar", default_value="Ошибка: неизвестный тип транспорта")
        return

    company.add_vehicle(vehicle)
    with dpg.table_row(parent="vehicles_table"):
        dpg.add_text(vehicle.vehicle_id)
        dpg.add_text(vtype)
        dpg.add_text(str(vehicle.capacity))
        dpg.add_text(str(vehicle.current_load))
        dpg.configure_item("status_bar", default_value="Транспорт добавлен")

def distribute_callback():
    company.optimize_cargo_distribution()
    dpg.configure_item("status_bar", default_value="Грузы распределены")

def export_callback():
    if not company.vehicles:
        dpg.configure_item("status_bar", default_value="Нет данных для экспорта")
        return
    with open("distribution_result.txt", "w", encoding="utf-8") as f:
        for v in company.vehicles:
            f.write(str(v) + "\n")
            for c in v.clients_list:
                f.write(f"  - {c.name}, груз: {c.cargo_weight}т, VIP: {c.is_vip}\n")
    dpg.configure_item("status_bar", default_value="Результат сохранён в distribution_result.txt")

# === Интерфейс ===
dpg.create_context()

# === Подключение шрифта с поддержкой кириллицы ===
with dpg.font_registry():
    default_font = dpg.add_font("C:/Windows/Fonts/arial.ttf", 16)
    # Явно добавляем диапазон символов кириллицы
    dpg.add_font_range(0x0400, 0x04FF, parent=default_font)
dpg.bind_font(default_font)

with dpg.window(label="Главное окно", width=800, height=600):
    # Меню
    with dpg.menu_bar():
        with dpg.menu(label="Файл"):
            dpg.add_menu_item(label="Экспорт результата", callback=export_callback)
        with dpg.menu(label="Справка"):
            dpg.add_menu_item(label="О программе", callback=show_about)

    # Панель управления
    dpg.add_button(label="Добавить клиента", callback=lambda: dpg.configure_item("add_client_window", show=True))
    dpg.add_button(label="Добавить транспорт", callback=lambda: dpg.configure_item("add_vehicle_window", show=True))
    dpg.add_button(label="Распределить грузы", callback=distribute_callback)

    # Таблицы
    with dpg.table(label="Клиенты", header_row=True, tag="clients_table"):
        dpg.add_table_column(label="Имя")
        dpg.add_table_column(label="Вес")
        dpg.add_table_column(label="Статус")

    with dpg.table(label="Транспорт", header_row=True, tag="vehicles_table"):
        dpg.add_table_column(label="ID")
        dpg.add_table_column(label="Тип")
        dpg.add_table_column(label="Грузоподъёмность")
        dpg.add_table_column(label="Загрузка")

    # Статусная строка
    dpg.add_text("", tag="status_bar")

# Окно "О программе"
with dpg.window(label="О программе", modal=True, show=False, tag="about_window"):
    dpg.add_text("ЛР12, Вариант X, Разработчик: Алексей")

# Окно добавления клиента
with dpg.window(label="Добавить клиента", modal=True, show=False, tag="add_client_window"):
    dpg.add_input_text(label="Имя клиента", tag="client_name")
    dpg.add_input_int(label="Вес груза", tag="client_weight")
    dpg.add_checkbox(label="VIP статус", tag="client_vip")
    dpg.add_button(label="Сохранить", callback=add_client_callback)
    dpg.add_button(label="Отмена", callback=lambda: dpg.configure_item("add_client_window", show=False))

# Окно добавления транспорта
with dpg.window(label="Добавить транспорт", modal=True, show=False, tag="add_vehicle_window"):
    dpg.add_combo(["Грузовик", "Поезд", "Самолёт"], label="Тип транспорта", tag="vehicle_type")
    dpg.add_input_int(label="Грузоподъёмность", tag="vehicle_capacity")
    dpg.add_input_int(label="Количество вагонов", tag="train_cars")
    dpg.add_input_int(label="Макс. высота полёта", tag="airplane_altitude")
    dpg.add_button(label="Сохранить", callback=add_vehicle_callback)
    dpg.add_button(label="Отмена", callback=lambda: dpg.configure_item("add_vehicle_window", show=False))

dpg.create_viewport(title="Логистическая компания", width=800, height=600)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()

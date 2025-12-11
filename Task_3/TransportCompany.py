import sys, os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from Task_2.Vehicle import Vehicle
from Task_1.Client import *
from Task_3.Train import train
from Task_3.Airplane import Airplane


class TransportCompany:
    def __init__(self, name):
        self.name = name
        self.vehicles = []
        self.clients = []

    def add_vehicle(self, vehicle):
        if isinstance(vehicle, Vehicle):
            self.vehicles.append(vehicle)
        else:
            print("Ошибка: объект не является транспортом")

    def list_vehicles(self):
        return self.vehicles

    def add_client(self, client):
        if isinstance(client, Client):
            self.clients.append(client)
        else:
            print("Ошибка: объект не является клиентом")

    def optimize_cargo_distribution(self):
        # Сортируем клиентов: VIP первыми
        sorted_clients = sorted(self.clients, key=lambda c: not c.is_vip)

        # Сортируем транспорт по вместимости (по убыванию)
        sorted_vehicles = sorted(self.vehicles, key=lambda v: v.capacity, reverse=True)

        for client in sorted_clients:
            for vehicle in sorted_vehicles:
                if vehicle.current_load + client.cargo_weight <= vehicle.capacity:
                    vehicle.load_cargo(client.cargo_weight)
                    vehicle.clients_list.append(client)
                    break
            else:
                print(f"Клиент {client.name} не помещается ни в один транспорт")

company = TransportCompany("ЛогистикПро")

# Добавляем транспорт
company.add_vehicle(Vehicle(150))
company.add_vehicle(train(200, 10))
company.add_vehicle(Airplane(100, 12000))

# Добавляем клиентов
company.add_client(Client("Иван", 50, True))
company.add_client(Client("Ольга", 80, False))
company.add_client(Client("VIP-Клиент", 120, True))

# Распределяем грузы
company.optimize_cargo_distribution()

# Выводим транспорт
for v in company.list_vehicles():
    print(v)
    for c in v.clients_list:
        print(f"  - Клиент: {c.name}, груз: {c.cargo_weight}, VIP: {c.is_vip}")
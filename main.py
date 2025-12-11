from Task_1.Client import Client
from Task_2.Vehicle import Vehicle
from Task_3.Train import train
from Task_3.Airplane import Airplane
from Task_3.TransportCompany import TransportCompany

def main_menu():
    company = TransportCompany("ЛогистикПро")

    while True:
        print("\n=== Меню логистической компании ===")
        print("1. Добавить клиента")
        print("2. Добавить транспорт")
        print("3. Показать список клиентов")
        print("4. Показать список транспорта")
        print("5. Распределить грузы")
        print("6. Вывести результат распределения")
        print("0. Выход")

        choice = input("Выберите опцию: ")

        if choice == "1":
            name = input("Имя клиента: ")
            weight = int(input("Вес груза: "))
            vip = input("VIP-клиент? (да/нет): ").lower() == "да"
            client = Client(name, weight, vip)
            company.add_client(client)
            print("Клиент добавлен.")

        elif choice == "2":
            print("Тип транспорта:")
            print("1. Vehicle")
            print("2. Train")
            print("3. Airplane")
            t_choice = input("Выберите тип: ")

            if t_choice == "1":
                cap = int(input("Грузоподъёмность: "))
                company.add_vehicle(Vehicle(cap))
            elif t_choice == "2":
                cap = int(input("Грузоподъёмность: "))
                cars = int(input("Количество вагонов: "))
                company.add_vehicle(train(cap, cars))
            elif t_choice == "3":
                cap = int(input("Грузоподъёмность: "))
                alt = int(input("Макс. высота полёта: "))
                company.add_vehicle(Airplane(cap, alt))
            else:
                print("Неверный тип транспорта.")
            print("Транспорт добавлен.")

        elif choice == "3":
            print("=== Клиенты ===")
            for c in company.clients:
                print(f"{c.name} — {c.cargo_weight}т, VIP: {c.is_vip}")

        elif choice == "4":
            print("=== Транспорт ===")
            for v in company.vehicles:
                print(v)

        elif choice == "5":
            company.optimize_cargo_distribution()
            print("Грузы распределены.")

        elif choice == "6":
            print("=== Результат распределения ===")
            for v in company.vehicles:
                print(v)
                for c in v.clients_list:
                    print(f"  - {c.name}, груз: {c.cargo_weight}т, VIP: {c.is_vip}")

        elif choice == "0":
            print("Выход.")
            break

        else:
            print("Неверный ввод.")
if __name__ == "__main__":
    main_menu()
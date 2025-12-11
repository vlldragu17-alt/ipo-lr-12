import sys, os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from Task_2.Vehicle import Vehicle
from Task_1.Client import *

class train(Vehicle):
    number_of_cars = None

    def __init__(self, capacity, number_of_cars):
        super().__init__(capacity)
        self.number_of_cars = number_of_cars
    def __str__(self):
        if self.capacity > self.current_load :
            return f"ID транспорта : {self.vehicle_id} , грузоподъёмность : {self.capacity}т. , текущая загрузка : {self.current_load}т. , кол-во вагонов : {self.number_of_cars}"
        else:
            return "Превышение грузоподъёмности"



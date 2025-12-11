import sys, os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from Task_2.Vehicle import Vehicle
from Task_1.Client import *

class Airplane(Vehicle):
    def __init__(self, capacity, max_altitude):
        super().__init__(capacity)
        self.max_altitude = max_altitude
        self.current_load = 0  # если не задаётся при создании

    def __str__(self):
        if self.current_load <= self.capacity:
            return f"ID самолёта: {self.vehicle_id}, грузоподъёмность: {self.capacity}т, текущая загрузка: {self.current_load}т, макс. высота полёта: {self.max_altitude}м"
        else:
            return "Превышение грузоподъёмности"
        
import sys, os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from Task_1.Client import *
#эт сверху костыль
import random
class Vehicle():

    def rand_id():
        #id
        Leters = ["A","B","C","D","E"]
        Numbers = [0,1,2,3,4,5,6,7,8,9]
        new_id = ""
        for i in range(2):
            new_id+=random.choice(Leters)
        for i in range(2,6):
            new_id+=str(random.choice(Numbers))
        return new_id

    vehicle_id = rand_id()
    capacity = None
    current_load = 0
    clients_list = None
    
    def __init__(self, capacity):
        self.capacity = capacity
        self.clients_list = []
    
    def load_cargo(self, cargo_weight):
        self.current_load += cargo_weight

    def __str__(self):
        if self.capacity > self.current_load :
            return f"ID транспорта : {self.vehicle_id} , грузоподъёмность : {self.capacity}т. , текущая загрузка : {self.current_load}т."
        else:
            return "Превышение грузоподъёмности"
        



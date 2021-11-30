from mesa import Model
# Debido a que necesitamos que existe un solo agente por celda, elegimos ''SingleGrid''.
from mesa.space import SingleGrid

# Con ''SimultaneousActivation, hacemos que todos los agentes se activen ''al mismo tiempo''.
from mesa.time import SimultaneousActivation

# Haremos uso de ''DataCollector'' para obtener información de cada paso de la simulación.
from mesa.datacollection import DataCollector

import numpy as np
import pandas as pd
from control_box_agent import ControlBoxAgent
from car_agent import CarAgent
from traffic_light_agent import TrafficLightAgent
import random

def get_grid(model):
    grid = np.zeros( (model.cars.width, model.cars.height) )
    for (_, x, y) in model.cars.coord_iter():
        content = model.cars.get_cell_list_contents((x, y))
        if content:
            grid[x][y] = 1
        else:
            grid[x][y] = 0
    return grid


class TrafficControlModel(Model):
    def __init__(self,numCars,numTrafficLights,maxCarsToPass,waitingLimit):
        self.trafficLights = SingleGrid(1,numTrafficLights, False)
        self.cars = SingleGrid(numTrafficLights,numCars, False)
        self.controlBox = ControlBoxAgent(1, self, maxCarsToPass)
        self.schedule = SimultaneousActivation(self)
        self.lastCar = 0
        self.waitingLimit = waitingLimit

        for (_, x, y) in self.trafficLights.coord_iter():
            a = TrafficLightAgent((x, y), self)
            self.trafficLights.place_agent(a, (x, y))
            self.schedule.add(a)

        self.datacollector = DataCollector(model_reporters={"Grid": get_grid})
        
    def step(self):
        destination = random.randint(0, 2)
        randomLane = random.randint(0, 3)

        a = CarAgent(self.lastCar, self, destination, self.waitingLimit, randomLane)
        content = self.cars.get_cell_list_contents((randomLane, 0))
        if not content:
            self.cars.place_agent(a, (randomLane, 0))
            self.lastCar+=1
        isGreen = False
        for i in range (self.trafficLights.height):
            cell = self.trafficLights.get_cell_list_contents((0, i))
            if cell and cell[0].lightColor == 1:
                isGreen = True
        if not isGreen:
            self.controlBox.optimumTrafficLight()

        self.datacollector.collect(self)
        self.schedule.step()


from mesa import Model
# Debido a que necesitamos que existe un solo agente por celda, elegimos ''SingleGrid''.
from mesa.space import SingleGrid

# Con ''SimultaneousActivation, hacemos que todos los agentes se activen ''al mismo tiempo''.
from mesa.time import SimultaneousActivation

# Haremos uso de ''DataCollector'' para obtener información de cada paso de la simulación.
from mesa.datacollection import DataCollector

import numpy as np
import pandas as pd
import ControlBoxAgent
import CarAgent
import TrafficLightAgent


class TrafficControlModel(Model):
    def __init__(self,numCars,numTrafficLights,maxCarsToPass):
        self.trafficLights = SingleGrid(1,numTrafficLights, False)
        self.cars = SingleGrid(numTrafficLights,numCars, False)
        self.controlBox = ControlBoxAgent(maxCarsToPass)
        self.schedule = SimultaneousActivation(self)

        for (_, x, y) in self.trafficLights.coord_iter():
            a = TrafficLightAgent((x, y), self)
            self.trafficLights.place_agent(a, (x, y))
            self.schedule.add(a)


        # for (_, x, y) in self.cars.coord_iter():
        #     a = CarAgent((x, y), self)
        #     self.cars.place_agent(a, (x, y))
        #     self.schedule.add(a)


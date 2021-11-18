from mesa import Model
# Debido a que necesitamos que existe un solo agente por celda, elegimos ''SingleGrid''.
from mesa.space import SingleGrid

# Con ''SimultaneousActivation, hacemos que todos los agentes se activen ''al mismo tiempo''.
from mesa.time import SimultaneousActivation

# Haremos uso de ''DataCollector'' para obtener información de cada paso de la simulación.
from mesa.datacollection import DataCollector

import numpy as np
import pandas as pd


class TrafficControlModel(Model):
    def __init__(self,width, height,numCars,numTrafficLights):
        self.numCars = numCars
        self.numTrafficLights
        self.grid = SingleGrid(width, height, True)
        self.schedule = SimultaneousActivation(self)



from _typeshed import Self
from mesa import Agent
# Debido a que necesitamos que existe un solo agente por celda, elegimos ''SingleGrid''.
    

import numpy as np
import pandas as pd

class ControlBoxAgent(Agent):
    def __init__(self, unique_id, model, trafficLights):
        super().__init__(unique_id, model)
        self.trafficLights = trafficLights
        self.cars = [0 for i in range(trafficLights)]
    def optimumTrafficLight():
        pass

    # color can be 0 for red or 1 for green
    def setTrafficLights(self,trafficLightIndex, color):
        self.trafficLights[trafficLightIndex].setLight(color)
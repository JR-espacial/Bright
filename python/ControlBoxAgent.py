
from _typeshed import Self
from mesa import Agent
from mesa import SingleGrid
    

import numpy as np
import pandas as pd

class ControlBoxAgent(Agent):
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
       
    def optimumTrafficLight():
        pass    

    # color can be 0 for red or 1 for green
    def setTrafficLights(self,trafficLightIndex, color):
        self.model.trafficLights[trafficLightIndex].setLight(color)
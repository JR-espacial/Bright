
from _typeshed import Self
from mesa import Agent
from mesa import SingleGrid
    

import numpy as np
import pandas as pd

class ControlBoxAgent(Agent):
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
       
    def optimumTrafficLight(self):

        chosenLane =-1
        laneSums =[]
        for lane in range(self.model.cars.height):
            laneSum =0.0
            for car in (self.model.cars.width):
                content = self.model.cars.get_cell_list_contents((lane,car))
                #if the cell has a car
                if content:
                    waitingTime =content[0].getWaitingTime()
                    laneSum += waitingTime
                    #if the car has exeded waiting limit turn the lane light green
                    if waitingTime >= content[0].waitingLimit:
                        chosenLane = lane
                        break
            laneSums.append(laneSum)
        

        #if no car has exeded waiting limit turn the lane with the max sum light green
        if chosenLane == -1:
            for i in range(len(laneSums)):
                if chosenLane == -1 or laneSums[i] > laneSums[chosenLane]:
                    chosenLane =i

        self.setTrafficLights(chosenLane)

       

    # color can be 0 for red or 1 for green
    def setTrafficLights(self,trafficLightIndex, color):
        self.model.trafficLights[trafficLightIndex].setLight(color)
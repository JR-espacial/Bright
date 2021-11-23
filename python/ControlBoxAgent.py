
from _typeshed import Self
from mesa import Agent
from mesa import SingleGrid
    

import numpy as np
import pandas as pd

class ControlBoxAgent(Agent):
    def __init__(self, unique_id, model,maxCarsToPass):
        super().__init__(unique_id, model)

        self.maxCarsToPass=maxCarsToPass

       
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

        greenTime =0
        carsToPass = laneSums[chosenLane]*.7
        for car in self.model.cars[chosenLane]:
            if greenTime < carsToPass:
                greenTime+=car.getWaitingTime()
                if greenTime>self.maxCarsToPass:
                    break

        self.turnTrafficLightGreen(chosenLane,1,greenTime)

       

    # color can be 0 for red or 1 for green
    def turnTrafficLightGreen(self,trafficLightIndex, color,time):
        self.model.trafficLights[trafficLightIndex].turnGreen(color,time)
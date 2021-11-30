
from mesa import Agent, Model
    
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
            for car in range (self.model.cars.width):
                content = self.model.cars.get_cell_list_contents((car,lane))
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
        
        #count the waiting time thats bein reduced
        gTime =0
        #initilize waiting reducccion that must pass 70% of the cars wating time unless there are more than maxCarsToPass
        waitingReduction = laneSums[chosenLane]*.7
        #ensure we dont exceed maxCarsToPass
        carsLeftToMax= self.maxCarsToPass

        for (_, x, y) in self.model.cars.coord_iter():
            content = self.model.cars.get_cell_list_contents((x, y))
            if content and y == chosenLane and carsLeftToMax and gTime < waitingReduction:
                gTime+=content[0].getWaitingTime()
                carsLeftToMax-=1
            else:
                break

        self.turnTrafficLightGreen(chosenLane,gTime)

       

    # color can be 0 for red or 1 for green
    def turnTrafficLightGreen(self,trafficLightIndex,gTime):
        content = self.model.trafficLights.get_cell_list_contents((0, trafficLightIndex))
        content[0].turnGreen(gTime)
        
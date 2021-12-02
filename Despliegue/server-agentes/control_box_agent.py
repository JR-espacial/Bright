
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
        carsWaiting =[]
        for lane in range(self.model.cars.width):
            laneSum = 0.0
            carWaitingLane = []
            for car in range (self.model.cars.height):
                content = self.model.cars.get_cell_list_contents((lane,car))
                #if the cell has a car
                if content:
                    waitingTime = content[0].getWaitingTime()
                    carWaitingLane.insert(0,waitingTime)
                    laneSum += waitingTime
                    #if the car has exeded waiting limit turn the lane light green
                    if waitingTime >= content[0].waitingLimit:
                        chosenLane = lane
            carsWaiting.append(carWaitingLane)
            
            laneSums.append(laneSum)
        
        
        #if no car has exeded waiting limit turn the lane with the max sum light green
        if chosenLane == -1:
            for i in range(len(laneSums)):
                if chosenLane == -1 or laneSums[i] > laneSums[chosenLane]:
                    chosenLane =i
        #initilize waiting reducccion that must pass 70% of the cars wating time unless there are more than maxCarsToPass
        waitingReduction = laneSums[chosenLane]*.7

        #print("waitingReduction",waitingReduction)
        #ensure we dont exceed maxCarsToPass
        carsLeftToMax= self.maxCarsToPass
        cars =0
        acumTime=0

        #print("laneSums",laneSums)
        #print("carsWaiting",carsWaiting)
       
        for waiting in carsWaiting[chosenLane]:
            if carsLeftToMax and acumTime < waitingReduction:
                #print("waiting",waiting)
                acumTime += waiting
                carsLeftToMax-=1
                cars +=1
            else:
                break

        self.model.carsToPass = cars

        
        #print("carstopass",self.model.carsToPass)

        self.turnTrafficLightGreen(chosenLane)

       

    # color can be 0 for red or 1 for green
    def turnTrafficLightGreen(self,trafficLightIndex):
        content = self.model.trafficLights.get_cell_list_contents((0, trafficLightIndex))
        content[0].turnGreen()
        self.model.greenLight = trafficLightIndex
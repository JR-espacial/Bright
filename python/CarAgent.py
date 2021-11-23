from mesa import Agent, model

import numpy as np
import pandas as pd
import time

class CarAgent(Agent):

    def __init__(self, unique_id, model, destination, location, destinationTime, waitingLimit, isMoving, lane):
        super().__init__(unique_id, model)
        self.destination = destination
        self.location = location
        self.destinationTime = destinationTime
        self.waitingLimit = waitingLimit
        self.startWaiting = 0.0
        self.isMoving = isMoving
        self.lane = lane

    def getWaitingTime(self):
        return time.time() - self.startWating

    def step(self):
        new_position = (self.pos[0]+1, self.pos[1])
        neighbour = self.model.cars.get_cell_list_contents(new_position)

        #Check trafficLight color if the car is at the middle of the street
        #Check if there is another car in front
        if (self.pos == self.model.cars.width/2 and self.model.trafficLights[self.lane].light == False) or len(neighbour) > 0:
            if self.isMoving:
                self.startWaiting = time.time()
                self.isMoving = False
        
        elif neighbour == 0:
            if self.pos[0] +1 == self.model.cars.width:
                self.self.model.cars.remove_agent(self.pos,self)
            else:
                self.model.cars.move_agent(self, new_position)

from mesa import Agent, model
# Debido a que necesitamos que existe un solo agente por celda, elegimos ''SingleGrid''.
    

import numpy as np
import pandas as pd

class CarAgent(Agent):

    def __init__(self, unique_id, model, destination, location, destinationTime, waitingTime, isMoving, lane):
        super().__init__(unique_id, model)
        self.destination = destination
        self.location = location
        self.destinationTime = destinationTime
        self.waitingTime = waitingTime
        self.isMoving = isMoving
        self.lane = lane

    def setDestination(self, destination):
        self.destination = destination

    def setLocation(self, location):
        self.location = location

    def setDestinationTime(self, destinationTime):
        self.destinationTime = destinationTime

    def setWaitingTime(self, waitingTime):
        self.waitingTime = waitingTime

    def setIsMoving(self, isMoving):
        self.isMoving = isMoving

    def step(self):
        new_position = (self.pos[0]+1, self.pos[1])
        neighbour = self.model.grid.get_cell_list_contents(new_position)
        #Check trafficLight color if the car is at the middle of the street
        #Check if there is another car in front
        if (self.pos == model.grid.width/2 and self.model.trafficLights[self.lane].light == False) or len(neighbour) > 0:
            self.isMoving = False
        elif neighbour == 0:
            self.model.grid.move_agent(self, new_position)

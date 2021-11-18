from mesa import Agent
# Debido a que necesitamos que existe un solo agente por celda, elegimos ''SingleGrid''.
    

import numpy as np
import pandas as pd

class CarAgent(Agent):

    def __init__(self, unique_id, model, destination, location, destinationTime, waitingTime, isMoving):
        super().__init__(unique_id, model)
        self.destination = destination
        self.location = location
        self.destinationTime = destinationTime
        self.waitingTime = waitingTime
        self.isMoving = isMoving

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

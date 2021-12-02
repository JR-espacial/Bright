from mesa import Model
# Debido a que necesitamos que existe un solo agente por celda, elegimos ''SingleGrid''.
from mesa.space import SingleGrid

# Con ''SimultaneousActivation, hacemos que todos los agentes se activen ''al mismo tiempo''.
from mesa.time import SimultaneousActivation

# Haremos uso de ''DataCollector'' para obtener información de cada paso de la simulación.
from mesa.datacollection import DataCollector

import json, logging, os, atexit


import numpy as np
import pandas as pd
from control_box_agent import ControlBoxAgent
from car_agent import CarAgent
from traffic_light_agent import TrafficLightAgent
import random
import time
import json

currentJson = ""

def get_grid(model):
    grid = np.zeros( (model.cars.width, model.cars.height) )
    for (_, x, y) in model.cars.coord_iter():
        content = model.cars.get_cell_list_contents((x, y))
        if content:
            grid[x][y] = 1
        else:
            grid[x][y] = 0
    return grid


class TrafficControlModel(Model):
    def __init__(self,numCars,numTrafficLights,maxCarsToPass,waitingLimit):
        self.trafficLights = SingleGrid(1,numTrafficLights, False)
        self.cars = SingleGrid(numTrafficLights,numCars, False)
        self.controlBox = ControlBoxAgent(1, self, maxCarsToPass)
        self.schedule = SimultaneousActivation(self)
        self.lastCar = 0
        self.waitingLimit = waitingLimit
        self.greenLight = -1
        self.startGreen = 0
        self.gTime = 0.003
        self.carsToPass=0
        self.carsToRemove = []
        self.slowCars = 0
        self.json = '{"values": ['

        for (_, x, y) in self.trafficLights.coord_iter():
            a = TrafficLightAgent((x, y), self)
            self.trafficLights.place_agent(a, (x, y))
            self.schedule.add(a)

        self.datacollector = DataCollector(model_reporters={"Grid": get_grid})
    
    def removeCar(self, agent):
        if(agent.lane == self.greenLight):
            self.carsToPass -=1
            #print(self.carsToPass)
        self.schedule.remove(agent)
        self.cars.remove_agent(agent)

    def generateJson(self):
        info = {
            "cars": [],
            "trafficLights": []
        }

        for lane in range(self.cars.width):
            for car in range (self.cars.height):
                content = self.cars.get_cell_list_contents((lane,car))
                if content:
                    dictionary = {"id":content[0].unique_id, "destiny":content[0].destination, "lane":content[0].lane, "isMoving":content[0].isMoving}
                    info["cars"].append(dictionary)

        for trafficLights in range(self.trafficLights.height):
            content = self.trafficLights.get_cell_list_contents((0,trafficLights))
            if content:
                dictionary = {"id":content[0].unique_id,"green":content[0].lightColor}
                info["trafficLights"].append(dictionary)

        self.json += json.dumps(info) + ","

        
    def step(self):
        if self.lastCar!=0: 
            self.generateJson()
        for car in self.carsToRemove:
            #print(len(self.carsToRemove),"carsToremove")
            self.removeCar(car)
            self.carsToRemove = []

        if self.slowCars == 0:
            self.slowCars = 6

            destination = random.randint(0, 2)
            randomLane = random.randint(0, 3)

            a = CarAgent(self.lastCar, self, destination, self.waitingLimit, randomLane)
            content = self.cars.get_cell_list_contents((randomLane, 0))
            if not content:
                self.cars.place_agent(a, (randomLane, 0))
                self.schedule.add(a)
                self.lastCar+=1
            if self.carsToPass <= 0:
                cell = self.trafficLights.get_cell_list_contents((0, self.greenLight))
                if(cell[0].lightColor==1):
                    self.startGreen = time.time()
                    cell[0].turnRed()

            passedTime =time.time()- self.startGreen
            #print("passedTime",passedTime)
            if self.greenLight == -1 or (self.carsToPass <= 0 and passedTime> self.gTime ):
                self.controlBox.optimumTrafficLight()

        self.slowCars -=1
        
        self.datacollector.collect(self)
        self.schedule.step()
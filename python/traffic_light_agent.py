from mesa import Agent,Model
import time

class TrafficLightAgent(Agent):
    def __init__(self, unique_id: int, model: Model) -> None:
        super().__init__(unique_id, model)
        self.lightColor = False

    def turnGreen(self, gTime: float):
        self.lightColor = True
        self.model.startGreen = time.time()
        # start = time.time()
        # while time.time()- start < gTime:
        #     pass
        # self.lightColor = False
    
    def getLight(self):
        return self.lightColor

    def turnRed(self):
        self.lightColor = False
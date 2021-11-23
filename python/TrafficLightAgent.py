from mesa import Agent,Model
import time

class TrafficLightAgent(Agent):
    def __init__(self, unique_id: int, model: Model, lightColor: True) -> None:
        super().__init__(unique_id, model)
        self.lightColor = lightColor

    def turnGreen(self, time: float):
        self.lightColor = True
        time.sleep(time)
        self.lightColor = False
    
    def getLight(self):
        return self.lightColor
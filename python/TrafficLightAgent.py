from mesa import Agent,Model
import time

class TrafficLightAgent(Agent):
    def __init__(self, unique_id: int, model: Model, lightColor: bool) -> None:
        super().__init__(unique_id, model)
        self.lightColor = lightColor

    def turnGreen(self, gTime: float):
        self.lightColor = True
        start = time.time()
        while time.time()- start < gTime:
            pass
        self.lightColor = False
    
    def getLight(self):
        return self.lightColor
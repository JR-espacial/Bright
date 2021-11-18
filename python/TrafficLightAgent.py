from mesa import Agent,Model
class TrafficLightAgent(Agent):
    def __init__(self, unique_id: int, model: Model,lightColor) -> None:
        super().__init__(unique_id, model)
        self.lightColor = lightColor

    def setLight(self,light):
        self.light = light
""" Importamos el modelo del archivo en que lo definimos. """
from traffic_control_model import TrafficControlModel

import matplotlib
import matplotlib.pyplot as plt
import matplotlib.animation as animation
plt.rcParams["animation.html"] = "jshtml"
matplotlib.rcParams['animation.embed_limit'] = 2**128

import numpy as np
import pandas as pd

import time
import datetime

NUM_CARS = 20
NUM_TRAFFIC_LIGHTS = 4
MAX_CARS = 10
WAITING_LIMIT = 5

MAX_TIME = 10

start_time = time.time()
model = TrafficControlModel(NUM_CARS, NUM_TRAFFIC_LIGHTS, MAX_CARS, WAITING_LIMIT)
frames = 0
while datetime.timedelta(seconds=(time.time() - start_time)< MAX_TIME):
    frames+=1
    model.step()

print('Tiempo de ejecución:', str(datetime.timedelta(seconds=(time.time() - start_time))))

all_grid = model.datacollector.get_model_vars_dataframe()

# Graficamos la información usando `matplotlib`
fig, axs = plt.subplots(figsize=(7,7))
axs.set_xticks([])
axs.set_yticks([])
patch = plt.imshow(all_grid.iloc[0][0], cmap=plt.cm.binary)

def animate(i):
    patch.set_data(all_grid.iloc[i][0])

anim = animation.FuncAnimation(fig, animate, frames=frames)
plt.show()
import matplotlib.pyplot as plt
import numpy as np
import random
import time


timeSteps = 100000
positionArrayX = np.ndarray(timeSteps)
positionArrayY = np.ndarray(timeSteps)

positionArrayX[0] = 0 
positionArrayY[0] = 0

choice = [0, 1, 2, 3, 4, 5, 6, 7]
fig, axs = plt.subplots(figsize=(6,6))
for timeStep in range(1, timeSteps):
    ranNum = random.choice(choice)
    positionArrayX[timeStep] = positionArrayX[timeStep-1]
    positionArrayY[timeStep] = positionArrayY[timeStep-1]
    if ranNum == 0:
        positionArrayX[timeStep] +=  1
    if ranNum == 1:
        positionArrayX[timeStep] += -1
    if ranNum == 2:
        positionArrayY[timeStep] +=  1
    if ranNum == 3:
        positionArrayY[timeStep] += -1
    if ranNum == 4:
        positionArrayY[timeStep] += 1
        positionArrayX[timeStep] += 1
    if ranNum == 5:
        positionArrayY[timeStep] += -1
        positionArrayX[timeStep] += -1  
    if ranNum == 6:
        positionArrayY[timeStep] += 1
        positionArrayX[timeStep] += -1
    if ranNum == 7:
        positionArrayY[timeStep] += -1
        positionArrayX[timeStep] += 1


axs.plot(positionArrayX, positionArrayY, color="k", linewidth=0.5)
fig.tight_layout()
plt.show()

        



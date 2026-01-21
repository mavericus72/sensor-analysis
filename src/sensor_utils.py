import numpy as np
import csv
np.random.seed(42)

time_steps = 1000
time = np.arange(time_steps)

temperature = np.random.normal(loc=80, scale=3,size=time_steps)
vibration = np.random.normal(loc=0.5, scale=0.05,size=time_steps)
rpm = np.random.normal(loc=2000, scale=50,size=time_steps)

temperature[700:800] += 25
vibration[720:780] += 0.4
rpm[750:850] += np.random.normal(0, 200, size=100)

with open("data/sensor_data.csv", mode="w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["time", "temperature", "vibration", "rpm"])
    for i in range(time_steps):
        writer.writerow([time[i], temperature[i], vibration[i], rpm[i]])


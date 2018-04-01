import matplotlib.pyplot as plt
import numpy as np


def read_datafile(file_name):
    x, y = np.loadtxt(file_name, delimiter=',')
    return x, y

xData, yData = read_datafile('someData.csv')

fig = plt.xkcd()

plt.title("Phase error before loop filter")
plt.xlabel('Time, s')
plt.ylabel('Phase estimation')

plt.text(0.7, -0.2,
        ("""Every day i'm huslin'
        ..."""))

plt.plot(xData, yData)

plt.show(fig)

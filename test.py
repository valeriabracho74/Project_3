import py_wake
import numpy as np
import matplotlib.pyplot as plt

from py_wake.examples.data.hornsrev1 import Hornsrev1Site, V80, wt_x, wt_y, wt16_x, wt16_y
from py_wake.literature.noj import Jensen_1983 as NOJ


#here we import the turbine, site and wake deficit model to use.
windTurbines = V80()
site = Hornsrev1Site()
noj = NOJ(site,windTurbines)
x = [0,0,100,200,300,400]
y = [30,40,50,60,70, 80]

x = np.arange(0,5000,200)
y = np.arange(0,5000,200)

plt.figure()
plt.scatter(x,y)
plt.show()

simulationResult = noj(x,y)
simulationResult.aep()
aep = simulationResult.aep().sum()
print (aep)

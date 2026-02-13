import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
"""
x = [1,2,3]
y = [3,2,0]

x_new = 2.5

y_new = np.interp(x_new, x,y)

print("Interpolated Value: ")
print(y_new)

plt.plot(x,y,'o-')
plt.show()


def linear_model(x, a, b):
    return a*x +b

x = [0,1,2,3,4,5]
y = [15,10,9,6,2,0]

popt, pcov = curve_fit(linear_model, x, y)
print(popt)
plt.plot(x,y, 'or')

xstart = -1
xstop = 6
increment = 0.1

xmodel = np.arange(xstart, xstop, increment)

a = popt[0]
b = popt[1]

ymodel = a*xmodel + b

plt.plot(xmodel, ymodel, 'b')

plt.show()
"""
x = [0, 1, 2, 3, 4, 5]
y = [15, 10, 9, 6, 2, 0]
plt.plot(x,y, 'or')
# Set Model order
model_order = 3
# Find Model
p = np.polyfit(x, y, model_order)
print(p)
# PlottheModel
xstart = -1
xstop = 6
increment = 0.1
xmodeldata = np.arange(xstart,xstop,increment)
ymodel = np.polyval(p, xmodeldata)
plt.plot(xmodeldata,ymodel)
plt.show()




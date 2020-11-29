import math
import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import quad

theta1 = 0.5
theta2 = 0.025
theta3 = 0.0125
D = 3


def model_CI(distance, deltat):
    return math.exp(-theta2*distance-theta1*deltat)


def model_CII(distance, deltat):
    num = theta1*deltat + 1
    den = pow( pow(theta1*deltat+1,2) + theta2*theta2*distance*distance, (D+1)/2)
    return num / den

def model_CIII(distance, deltat):
    return math.exp(-theta2*theta2*distance*distance - theta1*deltat - theta3*deltat*distance*distance)

def err(distance, dealtat):
    return 1 - math.exp(-2*theta2*distance-2*theta1*dealtat)

def tau_I(distance):
    return theta2*distance / theta1

def tau_II(distance):
    num = pow(1+theta2*theta2*distance*distance, 2/3)-1
    return num/theta1

def tau_III(distance):
    return theta2*theta2*distance*distance/theta1

x = np.linspace(0,100,100)
y1 = tau_I(x)
y2 = tau_II(x)
y3 = tau_III(x)
plt.figure()
plt.plot(x,y1, label="y1")
plt.plot(x,y2, linestyle="--", label="y2")
plt.plot(x,y3, linestyle=":", label="y3")
plt.legend(loc="upper left")
plt.show()

T=1
d2 = 10
x = np.linspace(0,1,100)

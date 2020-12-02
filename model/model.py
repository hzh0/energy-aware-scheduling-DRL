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
    return np.exp(-theta2*theta2*distance*distance - theta1*deltat - theta3*deltat*distance*distance)

def err(distance, dealtat):
    return 1 - np.exp(-2*theta2*distance-2*theta1*dealtat)

def tau_I(distance):
    return theta2*distance / theta1

def tau_II(distance):
    num = pow(1+theta2*theta2*distance*distance, 2/3)-1
    return num/theta1

def tau_III(distance):
    return (theta2*theta2*distance*distance)/theta1

x = np.linspace(0,100,100)
y1 = tau_I(x)
y2 = tau_II(x)
y3 = tau_III(x)
plt.figure()
plt.plot(x,y1, label="model1")
plt.plot(x,y2, linestyle="--", label="model2")
plt.plot(x,y3, linestyle=":", label="model3")
plt.legend(loc="upper left")
plt.show()

T = 1
distance = 10

t = np.linspace(0,T,1000)
t_delta1 = tau_I(10)
t_delta2 = tau_II(10)
t_delta3 = tau_III(10)
print(t_delta1)
print(t_delta2)
print(t_delta3)

def err_source1_model1(t):
    return 1 - np.exp(-2*theta2*0-2*theta1*t)

def err_source2_model1(t):
    return 1 - np.exp(-2*theta2*distance-2*theta1*(t-t_delta1))

def err_source1_model2(t):
    num = theta1 * t + 1
    den = pow(pow(theta1 * t + 1, 2) + theta2 * theta2 * 0 * 0, (D + 1) / 2)
    return 1- pow((num / den),2)

def err_source2_model2(t):
    num = theta1 * (t-t_delta2) + 1
    den = pow(pow(theta1 * (t-t_delta2) + 1, 2) + theta2 * theta2 * 10 * 10, (D + 1) / 2)
    return 1-pow((num / den),2)

def err_source1_model3(t):
    return 1 - pow(np.exp(-theta1 * t),2)

def err_source2_model3(t):
    return 1-pow(np.exp(-theta2*theta2 * 10 * 10 - theta1 * (t-t_delta3) - theta3 * (t-t_delta3) * 10 * 10),2)


GainI = []
t_deltasI = []

GainII = []
t_deltasII = []

GainIII = []
t_deltasIII = []

while (t_delta1 <= T):
    result1, err = quad(err_source1_model1,0,t_delta1)
    result2, err = quad(err_source2_model1,t_delta1,T)
    result = result1 + result2
    average_err_system = (1/T)*result
    average_err_sorce1, err = quad(err_source1_model1, 0,T)
    GainI.append(average_err_sorce1 / average_err_system)
    t_deltasI.append(t_delta1)
    t_delta1 += 0.001

while (t_delta2 <= T):
    result1, err = quad(err_source1_model2,0,t_delta2)
    result2, err = quad(err_source2_model2,t_delta2,T)
    result = result1 + result2
    average_err_system = (1/T)*result
    average_err_sorce1, err = quad(err_source1_model2, 0,T)
    GainII.append(average_err_sorce1 / average_err_system)
    t_deltasII.append(t_delta2)
    t_delta2 += 0.001

while (t_delta3 <= T):
    result1, err = quad(err_source1_model3,0,t_delta3)
    result2, err = quad(err_source2_model3,t_delta3,T)
    result = result1 + result2
    average_err_system = (1/T)*result
    average_err_sorce1, err = quad(err_source1_model3, 0,T)
    GainIII.append(average_err_sorce1 / average_err_system)
    t_deltasIII.append(t_delta3)
    t_delta3 += 0.001

plt.figure()
plt.plot(t_deltasI,GainI, label="model1")
plt.plot(t_deltasII,GainII, label="model2")
plt.plot(t_deltasIII,GainIII, label="model3")
plt.legend(loc="upper left")
plt.show()

import math
from numpy import *
import numpy as np

# 计算两个传感器间的欧式距离
def distance(pt1, pt2):
    return math.sqrt(math.pow(pt1[0]-pt2[0],2) + math.pow(pt1[1]-pt2[1],2))

# 计算两两传感器之间的距离
def get_all_distance():
    f = open("./intel_nodes_position.txt", "r")
    data = f.read().split('\n')
    for i in range(0, len(data)):
        if data[i][1] == ' ':
            data[i] = data[i][2:]
        elif data[i][2] == ' ':
            data[i] = data[i][3:]
        data[i] = data[i].split(", ")
        data[i][0] = float(data[i][0])
        data[i][1] = float(data[i][1])

    matrix = mat(zeros((55,55)))
    for i in range(0,55):
        matrix[0,i] = i
        matrix[i,0] = i
    for i in range(1,55):
        for j in range(1,55):
            if i == j:
                matrix[i,j] = 0
            else:
                matrix[i,j] = distance(data[i-1],data[j-1])
    np.savetxt("alldistance.csv", matrix, fmt="%.2f",delimiter = ',')
    return matrix

if __name__ == '__main__':
    get_all_distance()
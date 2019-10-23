'''
linear regresion
'''

import matplotlib.pyplot as plt
import random
from scipy.optimize import minimize
import numpy as np


N = 10
x_min = 0
x_max = 100
y_min = 0
y_max = 100


def getRandomData(n,xMin,xMax,yMin,yMax):
    l = []
    for i in range(0, n):
        l.append((random.randint(xMin, xMax), random.randint(yMin, yMax)))
    return l

def getDistance(data):
    sum_x_pow_2_i = 0
    sum_y_pow_2_i = 0
    sum_x_i_y_i = 0
    sum_x_i = 0
    sum_y_i = 0
    for d in data:
        x = d[0]
        y = d[1]
        sum_x_pow_2_i += x*x
        sum_y_pow_2_i += y*y
        sum_x_i_y_i += x*y
        sum_x_i += x
        sum_y_i += y
    return sum_x_pow_2_i, sum_y_pow_2_i, sum_x_i_y_i, sum_x_i, sum_y_i

def main():
    # plot ploints
    l = getRandomData(N, x_min, x_max, y_min, y_max)
    for point in l:
        plt.scatter(point[0], point[1])
        
    # calc line
    a,b,c,d,e = getDistance(l)
    print(getDistance(l))
    func = lambda x : a*x[0]**2 + b - 2*x[0]*c + 2*x[0]*x[1]*d - 2*x[1]*e + N*x[1]**2
    x0 = [2,3]
    res = minimize(func, x0, method='nelder-mead')
    print(res)
    
    # plot line
    plt.axis([-1,101,-1,101])
    m = res.x[0]
    p = res.x[1]
    x = np.linspace(-1,101,2)
    y = m*x+p

    print(f'y = {m} * x + {p}')
    
    plt.plot(x, y)
    plt.grid()
    plt.show()

main()



















    
